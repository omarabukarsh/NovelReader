# Novel Reader — Android PDF reader

A starter Android app built with Kotlin + Jetpack Compose. It imports one PDF into app-private storage, renders pages with Android `PdfRenderer`, saves the last page and cumulative reading time locally, and provides a basic 3D page-rotation effect.

## Requirements
- JDK 17
- Android SDK Platform 35 (for local Android Studio builds)
- Gradle 8.9 (the GitHub Actions workflow installs it)

## Build APK with GitHub Actions (no Android Studio required on your phone)
1. Create a GitHub repository, e.g. `NovelReader`.
2. Upload all files and folders from this project to the repository root. Keep `.github/workflows/build-apk.yml` at that exact path.
3. Open the repository's **Actions** tab.
4. Select **Build Android APK** → **Run workflow** (or push to `main`/`master`).
5. When the workflow finishes successfully, open its run and download the `NovelReader-debug-apk` artifact.
6. Extract the downloaded ZIP; it contains `app-debug.apk`.
7. Transfer the APK to your Android phone and install it. Android may ask you to allow installation from that source.

## Build locally
Open this folder in Android Studio, allow Gradle sync, then run **Build → Build Bundle(s) / APK(s) → Build APK(s)**. The output is `app/build/outputs/apk/debug/app-debug.apk`.

## Notes / current limitations
- This is a functional starter, not a polished production reader. The page animation is a Compose 3D rotation approximation, not a physically accurate curled paper mesh.
- It currently remembers the most recently opened PDF (copied into the app's private storage), the last page, and cumulative reading time. It does not yet provide a multi-book shelf.
- Reading time accumulates while the reader screen/app is active and pauses when the app goes to the background. The display refreshes on UI changes; a dedicated one-second ticker can be added for a perfectly live clock.
- Imported PDFs are copied into app-private storage. Android uninstalling the app removes those private copies and the saved statistics.
- PDF rendering is memory-intensive for very large pages. The initial implementation renders at 1400 px wide.
- No internet permission is requested; normal use is offline.
