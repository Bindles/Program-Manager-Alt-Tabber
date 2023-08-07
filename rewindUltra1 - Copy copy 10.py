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
    ("ctrl+r", "lambda: keyboard.send(f'open {program}')",
     "C:\Program Files\VideoLAN\VLC\vlc.exe")
]

# Add the hotkeys
for hotkey in hotkeys:
    key, action, program = hotkey
    keyboard.add_hotkey(key, eval(action))

# define the edit function


def edit_file(hotkeys):
    check_key = input("Change which key: ")
    for hotkey in hotkeys:
        key, action, program = hotkey
        if check_key == key:
            change_key = input(f"\033[34m{key}\033[0m {action} {program}")
            hotkey = (change_key, action, program)
            print(f"Key: {key}, Name: {action}, Book: {program}")
        elif check_key == action:
            change_key = input(f"\033[34m{key}\033[0m {action} {program}")
            hotkey = (key, change_key, program)
            print(f"Key: {key}, Name: {action}, Book: {program}")
        elif check_key == program:
            change_key = input(f"\033[34m{key}\033[0m {action} {program}")
            hotkey = (key, action, change_key)
            print(f"Key: {key}, Name: {action}, Book: {program}")


# define the hotkeys
keyboard.add_hotkey("ctrl+q", lambda: edit_file(hotkeys))
keyboard.add_hotkey(
    "ctrl+w", lambda: toggle_window_visibility(get_window_by_title("pyman1.exe")))

# print instructions on the screen
print("Edit: ctrl+q Hide: ctrl+w")

# create a flag to track whether the program is hidden or not
hidden =
