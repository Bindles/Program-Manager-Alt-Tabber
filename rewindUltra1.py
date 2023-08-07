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
keyboard.add_hotkey("ctrl+q", lambda: subprocess.call(["nano", "bong.txt"]))
keyboard.add_hotkey("ctrl+w", lambda: toggle_window_visibility(get_window_by_title("pyman1.exe")))

def get_window_by_title(title):
    """Get the window handle by title."""
    hwnd = user32.FindWindowW(None, title)
    if hwnd:
        return hwnd
    return None

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
