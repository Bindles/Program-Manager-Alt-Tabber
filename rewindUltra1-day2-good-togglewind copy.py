import ctypes
import subprocess
import keyboard

# get the console window handle
hwnd = ctypes.windll.kernel32.GetConsoleWindow()

# print instructions on the screen
print("Edit: ctrl+q Hide: ctrl+w")

# set the console title using the window handle
user32 = ctypes.WinDLL('user32')
user32.SetWindowTextW(hwnd, "pyman1.exe")

# hotkeys = [
# ["ctrl+q", "open, "["cmd", "/c", "notepad.exe", "bong.txt"]"]]
# ]

# define the hotkeys
keyboard.add_hotkey(
    "ctrl+q", lambda: subprocess.call(["cmd", "/c", "notepad.exe", "bong.txt"]))
keyboard.add_hotkey("ctrl+w", lambda: subprocess.call(["nano", "bong.txt"]))
keyboard.add_hotkey("ctrl+e", lambda: toggle_window_visibility(hwnd))

print(hwnd)


def toggle_window_visibility(hwnd):
    """Toggle the visibility of the window."""
    if not hwnd:
        return
    if user32.IsWindowVisible(hwnd):
        user32.ShowWindow(hwnd, 0)
    else:
        user32.ShowWindow(hwnd, 1)


# wait for hotkey press
keyboard.wait()
