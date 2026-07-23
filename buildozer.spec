[app]

title = DatingCallApp
package.name = datingcallapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,urllib3,certifi,chardet,idna
orientation = portrait
osx.kivy_version = 2.3.0
fullscreen = 0
android.permissions = INTERNET,CAMERA,RECORD_AUDIO
android.api = 33
android.minapi = 21
android.ndk_path = 
android.sdk_path = 
android.accept_sdk_license = True
p4a.branch = master
bootstraps = sdl2

[buildozer]

log_level = 2
warn_on_root = 1
