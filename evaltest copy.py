import keyboard
import win32gui
import win32process
import win32con

def get_window_by_title(title):
    """Get the window handle for the window with the given title."""
    def callback(hwnd, window_list):
        window_list.append(hwnd)

    window_list = []
    win32gui.EnumWindows(callback, window_list)
    for hwnd in window_list:
        if win32gui.GetWindowText(hwnd) == title:
            return hwnd
    return None

def toggle_window_visibility(hwnd):
    """Toggle the visibility of the window with the given handle."""
    if win32gui.IsWindowVisible(hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
    else:
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)

def edit_program_1():
    """Edit the values in the start.ini file."""
    # Read the start.ini file
    #with open("start.ini", "r") as f:
       # hotkey, action, program = f.read().strip().split(", ")

    # Get the new values from the user
    print("[1][2]")
    key_settings = keyboard.read_hotkey()
    if key_settings == "1":
        hotkey = input("Hotkey: ")
        action = input("Action: ")
        program = input("Program: ")

    # Write the new values to the start.ini file
    #with open("start.ini", "w") as f:
       # f.write(f"{hotkey}, {action}, {program}")

    # Set the hotkey
    keyboard.add_hotkey(hotkey, lambda: eval(action))

# Set the default values
hotkey = "ctrl+c"
action = "keyboard.send(f'explorer {program_1}')"
program = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"

# Set up the hotkeys
keyboard.add_hotkey("ctrl+z", lambda: toggle_window_visibility(get_window_by_title("opensesame")))
keyboard.add_hotkey("ctrl+x", lambda: exit())
keyboard.add_hotkey(hotkey, lambda: eval(action))
keyboard.add_hotkey("ctrl+s", lambda: edit_program_1())

# Start the event loop
try:
    # your code here
    keyboard.wait()
except KeyboardInterrupt:
    # handle the KeyboardInterrupt exception here
    print("Keyboard interrupt received, exiting program")
finally:
    # your cleanup code here
    pass
