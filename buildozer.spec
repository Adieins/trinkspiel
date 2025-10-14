[app]
title = Trinkspiel
package.name = trinkspiel
package.domain = org.adieins
source.dir = .
source.include_exts = py, kv, png, jpg, json
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
android.api = 34
android.minapi = 21
android.ndk = 26b
android.archs = arm64-v8a,armeabi-v7a
android.sdk_path = $HOME/.buildozer/android/platform/android-sdk
android.ndk_path = $HOME/.buildozer/android/platform/android-ndk