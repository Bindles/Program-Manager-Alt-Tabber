import ctypes
import subprocess
import keyboard

# get the console window handle
hwnd = ctypes.windll.kernel32.GetConsoleWindow()

# set the console title using the window handle
user32 = ctypes.WinDLL('user32')
user32.SetWindowTextW(hwnd, "pyman1.exe")

# print instructions on the screen
print("Edit: ctrl+q Hide: ctrl+w")

# define the hotkeys
keyboard.add_hotkey("ctrl+q", lambda: subprocess.call(["cmd", "/c", "nano.exe", "bong.txt"]))
keyboard.add_hotkey("ctrl+w", lambda: toggle_window_visibility(hwnd))

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