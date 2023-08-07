# Define the hotkeys
hotkeys = [
    ("ctrl+e", "lambda: keyboard.send(f'open {program}')", "C:\Program Files\Mozilla Firefox\firefox.exe"),
    ("ctrl+r", "lambda: keyboard.send(f'open {program}')", "C:\Program Files\VideoLAN\VLC\vlc.exe")
]

# Add the hotkeys
for hotkey in hotkeys:
    key, action, program = hotkey
    keyboard.add_hotkey(key, eval(action))
