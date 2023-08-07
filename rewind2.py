import keyboard
import subprocess

# print instructions on the screen
print("Edit[ctrl][q] Hide[ctrl][w]")

# create a flag to track whether the program is hidden or not
hidden = False

# register the hotkeys
keyboard.add_hotkey("ctrl+q", lambda: subprocess.Popen(["nano", "bong.txt"]))
keyboard.add_hotkey("ctrl+e", lambda: toggle_window_visibility())

def toggle_window_visibility():
    global hidden
    hidden = not hidden
    if hidden:
        # hide the program
        subprocess.Popen(["cmd", "/c", "taskkill", "/f", "/im", "python.exe"])
    else:
        # bring the program back
        subprocess.Popen(["python", "-i"], shell=True)

# keep the program running
while True:
    pass
