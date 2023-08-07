import ctypes
import subprocess
import keyboard

# get the console window handle
hwnd = ctypes.windll.kernel32.GetConsoleWindow()

# set the console title using the window handle
user32 = ctypes.WinDLL('user32')
user32.SetWindowTextW(hwnd, "pyman1.exe")

# define the hotkeys
keyboard.add_hotkey("ctrl+q", lambda: edit_file())
keyboard.add_hotkey("ctrl+w", lambda: toggle_window_visibility(get_window_by_title("pyman1.exe")))

# print instructions on the screen
print("Edit: ctrl+q Hide: ctrl+w")

# create a flag to track whether the program is hidden or not
hidden = False

# define the key, name, and book lists
keys = ["key1", "key2", "key3"]
names = ["name1", "name2", "name3"]
books = ["book1", "book2", "book3"]

# print the key, name, and book list with numbered items
for i in range(len(keys)):
    print(f"{i+1}. Key: {keys[i]}, Name: {names[i]}, Book: {books[i]}")

def edit_file():
    global keys, names, books
    check_key = input("Change which key: ")
    for i in range(len(keys)):
        if check_key == keys[i]:
            change_key = input(f"\033[34m{keys[i]}\033[0m {names[i]} {books[i]}")
            keys[i] = change_key
            print(f"Key: {keys[i]}, Name: {names[i]}, Book: {books[i]}")
        elif check_key == names[i]:
            change_key = input(f"\033[34m{keys[i]}\033[0m {names[i]} {books[i]}")
            names[i] = change_key
            print(f"Key: {keys[i]}, Name: {names[i]}, Book: {books[i]}")
        elif check_key == books[i]:
            change_key = input(f"\033[34m{keys[i]}\033[0m {names[i]} {books[i]}")
            books[i] = change_key
            print(f"Key: {keys[i]}, Name: {names[i]}, Book: {books[i]}")

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