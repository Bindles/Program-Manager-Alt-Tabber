import win32gui
import win32con
import win32api
import win32process

def list_windows():
    windows = []
    def enum_windows(hwnd, result):
        # Check if the window is visible and not minimized
        if win32gui.IsWindowVisible(hwnd) and not win32gui.IsIconic(hwnd):
            # Get the window title and process ID
            title = win32gui.GetWindowText(hwnd)
            pid = win32process.GetWindowThreadProcessId(hwnd)[1]
            # Add the window to the list
            windows.append((title, pid, hwnd))
    # Enumerate all top-level windows and pass them to the enum_windows function
    win32gui.EnumWindows(enum_windows, windows)
    return windows

def main():
    # List all major programs that are able to be alt-tabbed into
    windows = list_windows()
    # Display the list of programs
    for i, (title, pid, hwnd) in enumerate(windows):
        print(f"{i}: {title} ({pid}) ({hwnd})")
    # Get the user's selection
    selection = int(input("Enter the number of the program you want to select: "))
    # Get the selected program's name, process, and handle
    title, pid, hwnd = windows[selection]
    print(f"Selected program: {title} ({pid}) ({hwnd})")
    # Get the user's hotkey
    hotkey = input("Enter a 1 key or 2 key combination such as ctrl+g to use as a shortcut key: ")
    # Parse the hotkey
    keys = hotkey.split("+")
    mod = 0
    key = 0
    if "ctrl" in keys:
        mod |= win32con.MOD_CONTROL
    if "alt" in keys:
        mod |= win32con.MOD_ALT
    if "shift" in keys:
        mod |= win32con.MOD_SHIFT
    if "win" in keys:
        mod |= win32con.MOD_WIN
    if len(keys) == 1:
        # Get the virtual key code for the key
        key, shift = win32api.VkKeyScan(keys[0])
        if key < 0:
         print("Error: Invalid character")
        else:
        # Use the key and shift values as needed
            print(f"Key: {key}, Shift: {shift}")
         # Register the hotkey
    if not win32api.RegisterHotKey(None, 1, mod, key):
        print("Error registering hotkey")
    # Wait for the hotkey to be pressed
    print("Press the hotkey to bring the selected program to the front")
    try:
        msg = win32gui.GetMessage(None, 0, 0)
        while msg[0] != win32con.WM_HOTKEY:

            msg = win32gui.GetMessage(None, 0, 0)
        # Bring the selected program to the front
        win32gui.SetForegroundWindow(hwnd)
    finally:
        # Unregister the hotkey
        win32api.UnregisterHotKey(None, 1)

if __name__ == "__main__":
    main()
