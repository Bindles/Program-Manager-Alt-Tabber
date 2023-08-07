import keyboard

program_1 = ""

# check for start.ini file and get program_1 value
try:
    with open("start.ini", "r") as f:
        program_1 = f.readline().strip()
except FileNotFoundError:
    pass

# print instructions
print("Hide: [ctrl][z] Close: [ctrl][x] Open [ctrl][c] Edit [ctrl][s] that will stay on the screen.")

# key bindings
keyboard.add_hotkey("ctrl+z", lambda: keyboard.send("win+d"))
keyboard.add_hotkey("ctrl+x", lambda: exit())
keyboard.add_hotkey("ctrl+c", lambda: keyboard.send(f"explorer {program_1}"))
keyboard.add_hotkey("ctrl+s", lambda: edit_program_1())


def edit_program_1():
    print("[1] Edit Program 1")
    print("[2] Cancel")
    key_settings = keyboard.read_hotkey()
    if key_settings == "1":
        program_1 = input("Program 1: ")
        # check if input is a string
        if isinstance(program_1, str):
            # save program_1 value to start.ini file
            with open("start.ini", "w") as f:
                f.write(program_1)


try:
    # wait for key press
    keyboard.wait()
except KeyboardInterrupt:
    # handle keyboard interrupt exception
    print("Keyboard interrupt received, exiting program")
