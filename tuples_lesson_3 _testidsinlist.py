hotkeys = [["ctrl+e", "lambda: keyboard.send(f'open {program}')",     "C:\Program Files\Mozilla Firefox\firefox.exe"],
           ["ctrl+r", "lambda: keyboard.send(f'open {program}')",
            "C:\Program Files\VideoLAN\VLC\vlc.exe"]
           ]


for i, hotkey in enumerate(hotkeys):
    # hotkey.append(i)
    hotkeys_with_id = [i, *hotkey]
    print(hotkeys_with_id)
    # print(i, *hotkey)

print("blah")
print(hotkeys)
print("lookin id")
print(hotkeys[0][-2])
print(hotkeys[0][2])
