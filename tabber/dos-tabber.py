import keyboard
import win32gui

def bring_notepad_to_front():
    # Get the handle for the Notepad window
    notepad_handle = win32gui.FindWindow(None, "Untitled - Notepad")

    # Bring the Notepad window to the front
    win32gui.SetForegroundWindow(notepad_handle)

# Bind the Ctrl + A key combination to the bring_notepad_to_front function
keyboard.add_hotkey('ctrl+a', bring_notepad_to_front)

# Run the script indefinitely
while True:
    pass
