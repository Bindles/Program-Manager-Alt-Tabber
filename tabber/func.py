import psutil
import win32gui
import win32process
import keyboard

def get_process_info(process_name):
    # Get handle to window
    window_handle = win32gui.FindWindow(None, process_name)
    if not window_handle:
        return None, None

    # Get process ID
    _, process_id = win32process.GetWindowThreadProcessId(window_handle)

    return process_id, process_name

def assign_hotkey():
    # Wait for key input
    hotkey = keyboard.read_key()

    # Save hotkey
    global key1_hotkey
    key1_hotkey = hotkey

    # Parse process ID and name from selected item in combo box
    selected_item = combo_box.currentText()
    process_id, process_name = selected_item.split(' - ')

    # Save process ID and name
    global key1_process_id
    key1_process_id = int(process_id)
    global key1_process_name
    key1_process_name = process_name

    # Update text edit
    text_edit.setText(f'Process ID: {process_id}\nProcess Name: {process_name}\nHotkey: {hotkey}')

def bring_to_front():
    # Bring window with saved process ID to front
    window_handle = win32gui.FindWindow(None, key1_process_name)
    win32gui.SetForegroundWindow(window_handle)

# Initialize variables
key1_hotkey = None
key1_process_id = None
key1_process_name = None

# Set up hotkey to trigger bring_to_front function
keyboard.add_hotkey(key1_hotkey, bring_to_front)

# Connect button to assign_hotkey function
button.clicked.connect(assign_hotkey)
