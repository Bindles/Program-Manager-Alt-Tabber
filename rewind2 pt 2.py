import os
import keyboard
import subprocess

# print instructions on the screen
print("Edit[ctrl][q] Hide[ctrl][w]")

# create a flag to track whether the program is hidden or not
hidden = False

# register the hotkeys
keyboard.add_hotkey("ctrl+q", lambda: edit_file())
keyboard.add_hotkey("ctrl+e", lambda: toggle_window_visibility())

def edit_file():
    # check if bong.txt exists
    if not os.path.exists("bong.txt"):
        # create the file
        open("bong.txt", "a").close()
    # open bong.txt in the command terminal
    subprocess.Popen(["nano", "bong.txt"])

def toggle_window_visibility():
    global hidden
    hidden = not hidden
    if hidden:
        # hide the program
        subprocess.Popen(["cmd", "/c", "taskkill", "/f", "/im", "python.exe"])
    else:
        # bring the program back
        subprocess.call(["cmd", "/c", "start", "python", "-i"], shell=True)

# keep the program running
while True:
    pass
