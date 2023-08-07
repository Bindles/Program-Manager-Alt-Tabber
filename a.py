# DOS_TABBER_FULL: DOS PROCESSES MANAGER

from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QLabel, QLineEdit
import sys
import keyboard
import subprocess
import ctypes
import os
import configparser
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
    selection = int(
        input("Enter the number of the program you want to select: "))
    # Get the selected program's name, process, and handle
    title, pid, hwnd = windows[selection]
    print(f"Selected program: {title} ({pid}) ({hwnd})")
    # Get the user's hotkey
    hotkey = input(
        "Enter a 1 key or 2 key combination such as ctrl+g to use as a shortcut key: ")
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


# tuples_lesson_3_gsave_finished: change_key NEW, save, ..hotkeylist

# Function to save the hotkeys list to a file


def save(hotkeys):
    config = configparser.ConfigParser()
    config['HOTKEYS'] = {}
    for i, hotkey in enumerate(hotkeys):
        config['HOTKEYS'][f'hotkey{i}'] = ','.join(hotkey)
        # config['HOTKEYS'][f'hotkey{i}'] = ','.join([str(x) for x in hotkey])  # save after converting all to string
        # config['HOTKEYS'][f'hotkey{i}'] = ','.join(hotkey[:3]) #save only 3 elements
    with open('test01.ini', 'w') as configfile:
        config.write(configfile)

# Function to load the hotkeys list from a file


def load():
    config = configparser.ConfigParser()
    config.read('test01.ini')
    hotkeys = []
    for key in config['HOTKEYS']:
        hotkeys.append(config['HOTKEYS'][key].split(','))
    return hotkeys


# Initialize the hotkeys list
if os.path.exists('test01.ini'):
    hotkeys = load()
else:
    hotkeys = [
        ["ctrl+e", "lambda: keyboard.send(f'open {program}')",
         "C:\Program Files\Mozilla Firefox\firefox.exe"],
        ["ctrl+r", "lambda: keyboard.send(f'open {program}')",
         "C:\Program Files\VideoLAN\VLC\vlc.exe"]
    ]

# Print the hotkeys list
print(hotkeys)
# Get the index of the list or tuple to modify
index = int(input("Enter the index of the list or tuple to modify (0-1): "))
# Get the part of the list or tuple to modify
part = int(input("Enter the part of the list or tuple to modify (0-3): ")) - 1

if part == -1:
    print("penis")
    print(hotkeys[index][:])
    # Get user input for the new list or tuple
    value = input("Enter the new values separated by commas: ")
    # Split the input into a list
    value = value.split(',')
    # Check the length and types of the values
    if len(value) != 4:
        # Print an error message if the length is not 4
        print("Error: Incorrect number of values")
    elif not all(map(lambda x: x.isdigit(), value[3:])):
        # Print an error message if the fourth value is not an integer
        print("Error: Fourth value must be an integer")
    else:
        # Convert the elements to the correct type (if necessary)
        value = [int(x) if x.isdigit() else x for x in value]
        # Use slicing to replace the elements of the list or tuple at index `index` with the new values
        print(hotkeys[index][:])
        print(">>>>")
        hotkeys[index][:] = value
else:
    # Get user input for the new value
    value = input(f"Enter the new value of {hotkeys[index][part]} : ")
    # Convert the element to the correct type (if necessary)
    value = int(value) if value.isdigit() else value
    # Modify the element of the list or tuple
    print(hotkeys[index][part])
    print(">>>>")
    print(value)
    hotkeys[index][part] = value
    print(value)

# Print the modified list or tuple
print(hotkeys[index])
save(hotkeys)

# Print the entire list or tuple
print(value)
print(hotkeys)
print(f"my name is {value}what is your {part} right?")
print(f"my name is jon what is your {part} right?")


# RewindUltra 1 - Copy Copy 14: change_key orig, macros, hide functions (hide seld)

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
     "C:\Program Files\VideoLAN\VLC\vlc.exe"),
    ("ctrl+h", "lambda: subprocess.call({program})",
     ["cmd", "/c", "notepad.exe", "bong.txt"],)

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


# opses4 - coopy: open exes


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
    # key_settings = keyboard.read_hotkey()
    # if key_settings == "1":
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
keyboard.add_hotkey(
    "ctrl+z", lambda: toggle_window_visibility(get_window_by_title("opensesame")))
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


# ogwaytabber3copy: getprocess,gui


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.selected_process_id = None
        self.selected_process_name = None
        self.key1_hotkey = None
        self.key1_process_id = None
        self.key1_process_name = None
        self.key1_process_hwnd = None
        self.initUI()

    def initUI(self):
        # Create the process dropdown
        self.process_dropdown = QComboBox(self)
        self.process_dropdown.move(10, 10)
        self.process_dropdown.addItem("Select a process")
        self.process_dropdown.currentIndexChanged.connect(self.processSelected)

        # Get the list of major programs that can be selected with alt + tab
        major_programs = self.getMajorPrograms()
        # Add the programs to the dropdown
        for process_id, process_name in major_programs:
            self.process_dropdown.addItem(
                f"{process_name} ({process_id})", process_id)

        # Create the text form
        self.text_form = QLineEdit(self)
        self.text_form.move(10, 50)

        # Create the button
        self.button1 = QPushButton('Button 1', self)
        self.button1.move(10, 90)
        self.button1.clicked.connect(self.button1Clicked)

        # Create the labels to display the hotkey and process information
        self.key1_hotkey_label = QLabel(self)
        self.key1_hotkey_label.move(10, 130)
        self.key1_process_id_label = QLabel(self)
        self.key1_process_id_label.move(10, 150)
        self.key1_process_name_label = QLabel(self)
        self.key1_process_name_label.move(10, 170)

        self.setGeometry(300, 300, 250, 200)
        self.setWindowTitle('Originalway Tabber')
        self.show()

    def getMajorPrograms(self):
        def enumHandler(hwnd, lParam):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
                try:
                    handle = win32api.OpenProcess(
                        win32con.PROCESS_ALL_ACCESS, False, pid)
                    process_name = win32process.GetModuleFileNameEx(handle, 0)
                    if "\\" in process_name:
                        process_name = process_name.split("\\")[-1]
                    major_programs.append((pid, process_name))
                except:
                    pass

        major_programs = []
        win32gui.EnumWindows(enumHandler, None)
        return major_programs

    def processSelected(self):
        index = self.process_dropdown.currentIndex()
        self.selected_process_id = self.process_dropdown.itemData(index)
        self.selected_process_name = self.process_dropdown.currentText()

    def button1Clicked(self):
        if not self.selected_process_id:
            return
        hotkey = keyboard.read_hotkey()
        process_id = self.selected_process_id
        process_name = self.selected_process_name
        process_hwnd = self.selected_process_hwnd
        self.key1_hotkey = hotkey
        self.key1_process_id = process_id
        self.key1_process_name = process_name
        self.key1_hotkey_label.setText(f"Key 1 Hotkey: {self.key1_hotkey}")
        self.key1_process_id_label.setText(
            f"Key 1 Process ID: {self.key1_process_id}")
        self.key1_process_name_label.setText(
            f"Key 1 Process Name: {self.key1_process_name}")
        keyboard.add_hotkey(hotkey, self.key1Pressed)

    def key1Pressed(self):
        handle = win32api.OpenProcess(
            win32con.PROCESS_ALL_ACCESS, False, self.key1_process_id)
        win32gui.SetForegroundWindow(handle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
