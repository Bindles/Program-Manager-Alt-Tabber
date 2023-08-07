import ctypes
import subprocess
import keyboard

# define the hotkeys
hotkeys = [
    ["ctrl+r", "toggle", "C:\Program Files\VideoLAN\VLC\vlc.exe"],
    ["ctrl+h", "open", "notepad.exe"],
]


def get_action(argss):
    if argss == "open":
        print(action)
        return lambda: subprocess.call(program)
    if argss == "toggle":
        return lambda: subprocess.call  # toggle_window_visibility_by_hwnd


for hotkey in hotkeys:
    key, action, program = hotkey

    keyboard.add_hotkey(key, get_action(action))


keyboard.wait()
