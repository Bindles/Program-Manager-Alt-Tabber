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
    """Edit the value of program_1."""
    global program_1
    print("[1][2]")

def edit_program_1():
    """Edit the value of program_1."""
    global program_1
    print("[1][2]")
    ###key_settings = keyboard.read_hotkey()
    #if key_settings == "1":
    if 0 == 0:
        # Read the current value of program_1 from start.ini
        with open("start.ini", "r") as f:
            program_1 = f.readlines()[0].strip()
        # Prompt the user to enter a new value for program_1
        program_1 = input("Program 1: ")
        # Write the new value of program_1 to start.ini
        with open("start.ini", "w") as f:
            f.write(program_1)



# Set the default value of program_1
program_1 = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"

# Set up the hotkeys
keyboard.add_hotkey("ctrl+z", lambda: toggle_window_visibility(get_window_by_title("opensesame")))
keyboard.add_hotkey("ctrl+x", lambda: exit())
keyboard.add_hotkey("ctrl+c", lambda: keyboard.send(f"open {program_1}"))
keyboard.add_hotkey("ctrl+s", lambda: edit_program_1())

# Start the event loop
try:
    # your code here
    keyboard.wait()
except KeyboardInterrupt:
    # handle the KeyboardInterrupt exception here
    print("Keyboard interrupt received, exiting program")
finally:
    # this code will always be executed, regardless of whether or not an exception is raised
    print("Exiting program")
