import ctypes
import subprocess
import keyboard

# get the console window handle
hwnd = ctypes.windll.kernel32.GetConsoleWindow()

# set the console title using the window handle
user32 = ctypes.WinDLL('user32')
user32.SetWindowTextW(hwnd, "pyman1.exe")

# Define the hotkeys
hotkeys = [
    ("ctrl+e", "lambda: keyboard.send(f'open {program}')",
     "C:\Program Files\Mozilla Firefox\firefox.exe"),
    ("ctrl+r", "lambda: keyboard.send(f'open {program}')", "notepad.exe",),
    ("ctrl+k", "lambda: keyboard.send(f'open {program}')",
     "C:\Windows\system32\notepad.exe"),
    ["ctrl+p",
        "lambda: subprocess.call({program})", "notepad.exe"],
    ["ctrl+h", "lambda: subprocess.call(program)", "notepad.exe"]
]

# Add the hotkeys
for hotkey in hotkeys:
    key, action, program = hotkey
    keyboard.add_hotkey(key, eval(action))

# define the edit function


def edit_file(hotkeys):
    check_key = input("Change which key: ")
    for i in range(len(hotkeys)):
        hotkey = hotkeys[i]
        key, action, program = hotkey
        if check_key == key:
            print(hotkeys[i])
            type(hotkeys[i])
            change_key = input(f"\033[34m{key}\033[0m {action} {program}")
            hotkeys[i].key = change_key
        elif check_key == action:
            change_key = input(f"\033[34m{key}\033[0m {action} {program}")
            hotkeys[i] = (key, change_key, program)
        elif check_key == program:
            change_key = input(f"\033[34m{key}\033[0m {action} {program}")
            hotkeys[i] = (key, action, change_key)


# define the hotkeys
keyboard.add_hotkey("ctrl+q", lambda: edit_file(hotkeys))
keyboard.add_hotkey(
    "ctrl+w", lambda: toggle_window_visibility(get_window_by_title("pyman1.exe")))

# print instructions on the screen
print("Edit: ctrl+q Hide: ctrl+w")

# create a flag to track whether the program is hidden or not
hidden = False


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
