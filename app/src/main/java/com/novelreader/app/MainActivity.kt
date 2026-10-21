package com.novelreader.app

import android.content.Context
import android.graphics.Bitmap
import android.graphics.Color as AndroidColor
import android.graphics.pdf.PdfRenderer
import android.net.Uri
import android.os.Bundle
import android.os.ParcelFileDescriptor
import androidx.activity.ComponentActivity
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.compose.setContent
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.gestures.detectDragGestures
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableLongStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleEventObserver
import androidx.lifecycle.compose.LocalLifecycleOwner
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import java.io.File
import java.io.FileOutputStream
import java.util.Locale
import kotlin.math.abs
import kotlin.math.roundToInt

private val Ink = Color(0xFF1E293B)
private val Paper = Color(0xFFFFF8E9)
private val Navy = Color(0xFF172554)
private val Gold = Color(0xFFC49A52)

data class SavedBook(
    val title: String,
    val path: String,
    val page: Int,
    val totalPages: Int,
    val readMillis: Long
)

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { ReaderApp() }
    }
}

@Composable
private fun ReaderApp() {
    val context = LocalContext.current
    val prefs = remember { context.getSharedPreferences("novel_reader", Context.MODE_PRIVATE) }
    var book by remember { mutableStateOf(loadBook(prefs)) }
    var page by remember { mutableIntStateOf(book?.page ?: 0) }
    var totalPages by remember { mutableIntStateOf(book?.totalPages ?: 0) }
    var readMillis by remember { mutableLongStateOf(book?.readMillis ?: 0L) }
    var pageBitmap by remember { mutableStateOf<Bitmap?>(null) }
    var nextBitmap by remember { mutableStateOf<Bitmap?>(null) }
    var loading by remember { mutableStateOf(false) }
    var error by remember { mutableStateOf<String?>(null) }
    var isReading by remember { mutableStateOf(false) }
    var sessionStart by remember { mutableLongStateOf(0L) }
    var clockNow by remember { mutableLongStateOf(System.currentTimeMillis()) }
    var flipAngle by remember { mutableFloatStateOf(0f) }
    val scope = rememberCoroutineScope()
    val lifecycleOwner = LocalLifecycleOwner.current

    fun persist() {
        val active = book ?: return
        book = active.copy(page = page, totalPages = totalPages, readMillis = readMillis)
        prefs.edit()
            .putString("title", active.title)
            .putString("path", active.path)
            .putInt("page", page)
            .putInt("totalPages", totalPages)
            .putLong("readMillis", readMillis)
            .apply()
    }

    fun stopTimer() {
        if (isReading) {
            readMillis += (System.currentTimeMillis() - sessionStart).coerceAtLeast(0L)
            isReading = false
            persist()
        }
    }

    fun startTimer() {
        if (!isReading && book != null) {
            sessionStart = System.currentTimeMillis()
            isReading = true
        }
    }

    LaunchedEffect(isReading) {
        while (isReading) {
            clockNow = System.currentTimeMillis()
            delay(1000L)
        }
    }

    DisposableEffect(lifecycleOwner, book?.path) {
        val observer = LifecycleEventObserver { _, event ->
            if (event == Lifecycle.Event.ON_STOP && isReading) {
                readMillis += (System.currentTimeMillis() - sessionStart).coerceAtLeast(0L)
                isReading = false
                persist()
            }
        }
        lifecycleOwner.lifecycle.addObserver(observer)
        onDispose {
            lifecycleOwner.lifecycle.removeObserver(observer)
            if (isReading) {
                readMillis += (System.currentTimeMillis() - sessionStart).coerceAtLeast(0L)
                isReading = false
                persist()
            }
        }
    }

    val pdfPicker = rememberLauncherForActivityResult(ActivityResultContracts.OpenDocument()) { uri: Uri? ->
        if (uri != null) {
            scope.launch {
                loading = true
                error = null
                try {
                    stopTimer()
                    val copied = withContext(Dispatchers.IO) { copyPdfToPrivateStorage(context, uri) }
                    val info = withContext(Dispatchers.IO) { inspectPdf(copied) }
                    book = SavedBook(info.first, copied.absolutePath, 0, info.second, 0L)
                    page = 0
                    totalPages = info.second
                    readMillis = 0L
                    prefs.edit().clear().putString("title", info.first).putString("path", copied.absolutePath)
                        .putInt("page", 0).putInt("totalPages", info.second).putLong("readMillis", 0L).apply()
                    startTimer()
                } catch (t: Throwable) {
                    error = "تعذّر فتح الملف. تأكد أنه ملف PDF صالح."
                } finally {
                    loading = false
                }
            }
        }
    }

    LaunchedEffect(book?.path, page) {
        val current = book ?: run { pageBitmap = null; nextBitmap = null; return@LaunchedEffect }
        loading = true
        try {
            val pair = withContext(Dispatchers.IO) {
                val file = File(current.path)
                if (!file.exists()) throw IllegalStateException("PDF missing")
                val fd = ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY)
                PdfRenderer(fd).use { renderer ->
                    val currentPage = renderPage(renderer, page.coerceIn(0, renderer.pageCount - 1))
                    val following = if (page + 1 < renderer.pageCount) renderPage(renderer, page + 1) else null
                    currentPage to following
                }
            }
            pageBitmap = pair.first
            nextBitmap = pair.second
            totalPages = current.totalPages
            persist()
        } catch (_: Throwable) {
            if (book != null) error = "لم أستطع قراءة صفحات هذا الملف."
        } finally {
            loading = false
        }
    }

    MaterialTheme {
        Surface(modifier = Modifier.fillMaxSize(), color = Color(0xFFF3EEE4)) {
            Column(
                modifier = Modifier.fillMaxSize().padding(horizontal = 18.dp, vertical = 16.dp),
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.SpaceBetween
                ) {
                    Column {
                        Text("NOVEL READER", color = Navy, fontSize = 12.sp, fontWeight = FontWeight.Bold, letterSpacing = 2.sp)
                        Text("مكتبتك، على طريقتك", color = Ink, fontSize = 20.sp, fontWeight = FontWeight.SemiBold)
                    }
                    Text("PDF", color = Gold, fontSize = 13.sp, fontWeight = FontWeight.Bold)
                }
                Spacer(Modifier.height(16.dp))
                if (book == null) {
                    EmptyLibrary(
                        loading = loading,
                        onPick = { pdfPicker.launch(arrayOf("application/pdf")) }
                    )
                } else {
                    val currentBook = book!!
                    Text(currentBook.title, color = Ink, fontSize = 16.sp, fontWeight = FontWeight.SemiBold,
                        textAlign = TextAlign.Center, maxLines = 2)
                    Spacer(Modifier.height(8.dp))
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Text("الوقت المقروء", color = Color(0xFF64748B), fontSize = 12.sp)
                        Spacer(Modifier.width(8.dp))
                        Text(formatDuration(readMillis + if (isReading) (clockNow - sessionStart).coerceAtLeast(0L) else 0L),
                            color = Navy, fontWeight = FontWeight.Bold, fontSize = 14.sp)
                    }
                    Spacer(Modifier.height(12.dp))
                    Box(
                        modifier = Modifier.weight(1f).fillMaxWidth(),
                        contentAlignment = Alignment.Center
                    ) {
                        Row(
                            modifier = Modifier.fillMaxWidth().padding(horizontal = 3.dp),
                            horizontalArrangement = Arrangement.Center,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            BookPage(
                                bitmap = pageBitmap,
                                nextBitmap = nextBitmap,
                                modifier = Modifier.weight(1f),
                                fallbackText = if (loading) "جارٍ تحميل الصفحة…" else "الصفحة ${page + 1}",
                                angle = flipAngle,
                                onDrag = { delta -> flipAngle = (flipAngle + delta * 0.7f).coerceIn(-180f, 180f) },
                                onDragEnd = {
                                    val oldAngle = flipAngle
                                    scope.launch {
                                        if (oldAngle < -55f && page < totalPages - 1) {
                                            Animatable(oldAngle).animateTo(-180f, tween(180))
                                            page += 1
                                            persist()
                                        } else if (oldAngle > 55f && page > 0) {
                                            page -= 1
                                            persist()
                                        }
                                        flipAngle = 0f
                                    }
                                }
                            )
                        }
                    }
                    Text("اسحب الصفحة إلى اليسار أو اليمين للتقليب", color = Color(0xFF64748B), fontSize = 11.sp)
                    Spacer(Modifier.height(8.dp))
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        OutlinedButton(onClick = {
                            if (page > 0) { page--; persist() }
                        }, enabled = page > 0) { Text("السابق") }
                        Text("${page + 1} / $totalPages", color = Ink, fontWeight = FontWeight.Medium)
                        Button(onClick = {
                            if (page < totalPages - 1) { page++; persist() }
                        }, enabled = page < totalPages - 1) { Text("التالي") }
                    }
                    Spacer(Modifier.height(10.dp))
                    OutlinedButton(onClick = { stopTimer(); pdfPicker.launch(arrayOf("application/pdf")) }, modifier = Modifier.fillMaxWidth()) {
                        Text("فتح رواية PDF أخرى")
                    }
                }
                if (error != null) {
                    Spacer(Modifier.height(8.dp))
                    Text(error!!, color = Color(0xFFB91C1C), fontSize = 12.sp, textAlign = TextAlign.Center)
                }
                Spacer(Modifier.height(8.dp))
                Text("تُحفظ الروايات ومدة القراءة على هذا الجهاز فقط", color = Color(0xFF64748B), fontSize = 10.sp)
            }
        }
    }
}

@Composable
private fun EmptyLibrary(loading: Boolean, onPick: () -> Unit) {
    Column(
        modifier = Modifier.fillMaxSize(),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Box(
            modifier = Modifier.size(150.dp).shadow(12.dp, RoundedCornerShape(16.dp))
                .clip(RoundedCornerShape(16.dp))
                .background(Brush.linearGradient(listOf(Navy, Color(0xFF3B82F6)))),
            contentAlignment = Alignment.Center
        ) {
            Column(horizontalAlignment = Alignment.CenterHorizontally) {
                Text("📖", fontSize = 52.sp)
                Text("READ", color = Color.White, fontSize = 12.sp, fontWeight = FontWeight.Bold, letterSpacing = 3.sp)
            }
        }
        Spacer(Modifier.height(24.dp))
        Text("ابدأ روايتك الأولى", fontSize = 22.sp, fontWeight = FontWeight.Bold, color = Navy)
        Spacer(Modifier.height(8.dp))
        Text("افتح ملف PDF واقرأه ككتاب،\nمع تسجيل إجمالي وقت القراءة تلقائيًا.",
            color = Color(0xFF64748B), textAlign = TextAlign.Center, lineHeight = 22.sp)
        Spacer(Modifier.height(22.dp))
        Button(onClick = onPick, enabled = !loading) {
            Text(if (loading) "جارٍ التحضير…" else "اختيار ملف PDF")
        }
    }
}

@Composable
private fun BookPage(
    bitmap: Bitmap?,
    nextBitmap: Bitmap?,
    modifier: Modifier = Modifier,
    fallbackText: String,
    angle: Float,
    onDrag: (Float) -> Unit,
    onDragEnd: () -> Unit
) {
    Box(
        modifier = modifier
            .fillMaxWidth()
            .aspectRatio(0.70f)
            .padding(2.dp)
            .shadow(12.dp, RoundedCornerShape(topStart = 3.dp, topEnd = 10.dp, bottomEnd = 8.dp, bottomStart = 3.dp))
            .clip(RoundedCornerShape(topStart = 3.dp, topEnd = 10.dp, bottomEnd = 8.dp, bottomStart = 3.dp))
            .background(Paper),
        contentAlignment = Alignment.Center
    ) {
        if (nextBitmap != null && !nextBitmap.isRecycled) {
            Image(
                bitmap = nextBitmap.asImageBitmap(),
                contentDescription = "الصفحة التالية",
                modifier = Modifier.fillMaxSize()
            )
        }
        if (bitmap != null && !bitmap.isRecycled) {
            Image(
                bitmap = bitmap.asImageBitmap(),
                contentDescription = "صفحة PDF",
                modifier = Modifier.fillMaxSize().graphicsLayer {
                    rotationY = angle
                    cameraDistance = 18 * density
                    shadowElevation = if (abs(angle) > 5) 18f else 0f
                    transformOrigin = androidx.compose.ui.graphics.TransformOrigin(if (angle < 0) 1f else 0f, 0.5f)
                }
            )
        } else {
            Text(fallbackText, color = Ink, textAlign = TextAlign.Center, modifier = Modifier.padding(18.dp))
        }
        Canvas(Modifier.fillMaxSize()) {
            drawRect(
                brush = Brush.horizontalGradient(
                    colors = listOf(Color.Black.copy(alpha = 0.03f), Color.Transparent, Color.Black.copy(alpha = 0.05f))
                )
            )
        }
        Box(
            modifier = Modifier.fillMaxSize().pointerInput(Unit) {
                detectDragGestures(
                    onDragEnd = onDragEnd,
                    onDragCancel = onDragEnd
                ) { change, dragAmount ->
                    change.consume()
                    onDrag(dragAmount.x)
                }
            }
        )
    }
}

private fun copyPdfToPrivateStorage(context: Context, uri: Uri): File {
    val input = context.contentResolver.openInputStream(uri) ?: error("Cannot open URI")
    val folder = File(context.filesDir, "books").apply { mkdirs() }
    val file = File(folder, "novel_${System.currentTimeMillis()}.pdf")
    input.use { source ->
        FileOutputStream(file).use { output -> source.copyTo(output) }
    }
    val displayName = uri.lastPathSegment?.substringAfterLast('/')?.substringAfterLast(':') ?: "رواية PDF"
    return file
}

private fun inspectPdf(file: File): Pair<String, Int> {
    val fd = ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY)
    val count = PdfRenderer(fd).use { it.pageCount }
    return file.nameWithoutExtension.replace('_', ' ') to count
}

private fun renderPage(renderer: PdfRenderer, index: Int): Bitmap {
    renderer.openPage(index).use { pdfPage ->
        val maxWidth = 1400
        val scale = maxWidth.toFloat() / pdfPage.width.toFloat()
        val width = maxWidth
        val height = (pdfPage.height * scale).roundToInt().coerceAtLeast(1)
        val bitmap = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888)
        bitmap.eraseColor(AndroidColor.WHITE)
        pdfPage.render(bitmap, null, null, PdfRenderer.Page.RENDER_MODE_FOR_DISPLAY)
        return bitmap
    }
}

private fun loadBook(prefs: android.content.SharedPreferences): SavedBook? {
    val path = prefs.getString("path", null) ?: return null
    val file = File(path)
    if (!file.exists()) return null
    return SavedBook(
        title = prefs.getString("title", file.nameWithoutExtension) ?: file.nameWithoutExtension,
        path = path,
        page = prefs.getInt("page", 0),
        totalPages = prefs.getInt("totalPages", 0),
        readMillis = prefs.getLong("readMillis", 0L)
    )
}

private fun formatDuration(millis: Long): String {
    val seconds = millis.coerceAtLeast(0L) / 1000L
    val hours = seconds / 3600L
    val minutes = (seconds % 3600L) / 60L
    val secs = seconds % 60L
    return String.format(Locale.getDefault(), "%02d:%02d:%02d", hours, minutes, secs)
}
