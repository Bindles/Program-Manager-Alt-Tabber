import keyboard
import ctypes
from functools import partial


def bring_to_front(hwnd):
    # Bring the window to the front
    ctypes.windll.user32.SetForegroundWindow(hwnd)


def get_hwnd(program):
    # Get the hwnd of the program
    hwnd = ctypes.windll.user32.FindWindowW(None, program)
    # Check if the program was found
    if hwnd == 0:
        print(f"Error: Could not find {program}")
        return None
    else:
        bring_to_front(hwnd)
        return hwnd


# Initialize the hotkeys list
hotkeys = [
    ["ctrl+e", "bring_to_front", "Untitled - Notepad", None],
    ["ctrl+r", "bring_to_front", "VLC media player", None]
]


def redraw_keys():
    for hotkey in hotkeys:
        key, action, program, hwnd_id = hotkey
        if action == "bring_to_front" and hwnd_id is not None:
            # Use partial to capture the value of hwnd_id
            hotkey_func = partial(bring_to_front, hwnd_id)
            keyboard.add_hotkey(key, hotkey_func)
        elif action == "bring_to_front":
            # Use partial to capture the value of program
            hotkey_func = partial(get_hwnd, program)
            keyboard.add_hotkey(key, hotkey_func)
            # Update the hotkeys list with the hwnd value
            hotkey[-1] = hwnd_id


# Register the hotkeys
redraw_keys()

# Start the keyboard listener
keyboard.wait()
