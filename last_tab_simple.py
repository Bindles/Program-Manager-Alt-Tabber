import ctypes
import keyboard

# List of hotkeys and their actions
hotkeys = [
    ["ctrl+e", "open", "notepad"],
    ["ctrl+r", "open", "vlc media player"],
    ["ctrl+t", "bring_to_front", "Untitled - Notepad"],
    ["ctrl+y", "bring_to_front", "vlc media player"]
]

# Function to open a program


def open_program(program):
    # Use the `os` library to open the program
    import os
    os.startfile(program)

# Function to bring a program to the front


def bring_to_front(program):
    # Use `ctypes` to get the handle of the program window
    hwnd = ctypes.windll.user32.FindWindowW(None, program)
    print(f"bringtofront {hwnd}")
    # Use `ctypes` to bring the window to the front
    ctypes.windll.user32.SetForegroundWindow(hwnd)


# Iterate over the hotkeys and set up the appropriate action
for hotkey in hotkeys:
    key, action, program = hotkey
    if action == "open":
        # Set up a hotkey to open the program
        keyboard.add_hotkey(key, open_program, args=(program,))
        print(hotkey)
    elif action == "bring_to_front":
        # Set up a hotkey to bring the program to the front
        keyboard.add_hotkey(key, bring_to_front, args=(program,))
        print(hotkey)


# Run the program in the background
keyboard.wait()
