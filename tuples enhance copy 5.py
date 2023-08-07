import ctypes
import subprocess
import keyboard

# define the hotkeys
hotkeys = [
    ["ctrl+r", "toggle", "C:\Program Files\VideoLAN\VLC\vlc.exe"],
    ["ctrl+h", "open", "notepad.exe"],
]


def get_action(arg):
    if arg == "open":
        return lambda: subprocess.call()
    # if arg == "toggle":
       # return lambda program: subprocess.call #toggle_window_visibility_by_hwnd


for hotkey in hotkeys:
    key, action, program = hotkey
    print(key)
    print(get_action(action))
    print(program)
    # keyboard.add_hotkey(key, get_action(action)(program))


keyboard.wait()
