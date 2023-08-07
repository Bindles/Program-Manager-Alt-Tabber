import os
import keyboard
import subprocess
import win32gui
import win32con
import setproctitle

setproctitle.setproctitle("pyman1.exe")

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
        subprocess.Popen(["cmd", "/c", "taskkill", "/f", "/im", "pyman1.exe"])
    else:
        # bring the program back
        bring_to_front()

def bring_to_front():
    # get the handle of the current instance of the Python interpreter
    hwnd = win32gui.FindWindow(None, "pyman1.exe")
    # set the window as the foreground window
    win32gui.SetForegroundWindow(hwnd)

# keep the program running
while True:
    pass
