[app]
title = HMD
package.name = trinkspiel
package.domain = org.example
source.dir = .
source.main = main.py
version = 1.0
orientation = portrait
fullscreen = 0
icon.filename = icon.png

# Wichtig: Kivy ist nötig
requirements = python3,kivy

# Falls du zusätzliche Dateien nutzt:
include_patterns = game.py,game.kv

[buildozer]
log_level = 2
warn_on_root = 1