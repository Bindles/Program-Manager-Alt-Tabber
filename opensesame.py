import keyboard
import os

# Check for start.ini file and assign value to program_1
if os.path.exists('start.ini'):
    with open('start.ini', 'r') as f:
        program_1 = f.read()
else:
    program_1 = "C:\Program Files\VideoLAN\VLC\vlc.exe"

# Print instructions
print("Hide: [ctrl][z] Close: [ctrl][x] Open [ctrl][c] Edit [ctrl][a] that will stay on the screen.")

# Define functions for each keyboard shortcut
def hide_program():
    keyboard.send('alt+tab')

def close_program():
    exit()

def open_program_1():
    os.startfile(program_1)

def edit_start_ini():
    with open('start.ini', 'w') as f:
        f.write(input("Enter the new location for program 1: "))

# Register keyboard shortcuts
keyboard.add_hotkey('ctrl+z', hide_program)
keyboard.add_hotkey('ctrl+x', close_program)
keyboard.add_hotkey('ctrl+c', open_program_1)
keyboard.add_hotkey('ctrl+a', edit_start_ini)

# Wait for keyboard shortcuts to be triggered
try:
    # your code here
    keyboard.wait()
except KeyboardInterrupt:
    # handle the KeyboardInterrupt exception here
    print("Keyboard interrupt received, exiting program")
finally:
    # this code will always be executed, regardless of whether or not an exception is raised
    print("Exiting program")
