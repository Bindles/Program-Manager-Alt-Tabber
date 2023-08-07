import keyboard
import subprocess

# print instructions on the screen
print("Edit[ctrl][q] Hide[ctrl][w]")

# create a flag to track whether the program is hidden or not
hidden = False

# listen for keypresses
while True:
    # check for ctrl+q
    if keyboard.is_pressed("ctrl+q"):
        # open bong.txt in the command terminal
        subprocess.Popen(["nano", "bong.txt"])

    # check for ctrl+e
    elif keyboard.is_pressed("ctrl+e"):
        # toggle the hidden flag
        hidden = not hidden
        if hidden:
            # hide the program
            subprocess.Popen(["cmd", "/c", "taskkill", "/f", "/im", "python.exe"])
        else:
            # bring the
