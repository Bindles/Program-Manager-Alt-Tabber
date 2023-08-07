import keyboard
import ctypes


def bring_to_front(hwnd):
    # Bring the window to the front
    ctypes.windll.user32.SetForegroundWindow(hwnd)


def get_hwnd(program):
    # Get the hwnd of the program
    hwnd = ctypes.windll.user32.FindWindowW(None, program)
    # Check if the program was found
    if hwnd == 0:
        print(f"Error: Could not find {program}")
    else:
        bring_to_front(hwnd)
        return hwnd


# Initialize the hotkeys list
hotkeys = [
    ["ctrl+e", "bring_to_front", "Untitled - Notepad", None],
    ["ctrl+r", "bring_to_front", "VLC media player", None]
]

for hotkey in hotkeys:
    key, action, program, hwnd_id = hotkey
    if action == "bring_to_front" and hwnd_id is not None:
        keyboard.add_hotkey(key, lambda: bring_to_front(hwnd_id))
        print(hotkey)
    else:
        hwnd_id = get_hwnd(program)
        hotkey[-1] = hwnd_id
        keyboard.add_hotkey(key, lambda: bring_to_front(hwnd_id))
        print(hotkey)

# Start the keyboard listener
keyboard.wait()
