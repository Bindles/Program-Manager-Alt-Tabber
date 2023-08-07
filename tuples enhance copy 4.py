import ctypes
import subprocess
import keyboard

# define the hotkeys
keyboard.add_hotkey("ctrl+q", lambda: edit_file(hotkeys))

# Define the hotkeys
hotkeys = [
    ["ctrl+e", "lambda: keyboard.send(f'open {program}')",
     "C:\Program Files\Mozilla Firefox\firefox.exe",],
    ["ctrl+r", "lambda: keyboard.send(f'open {program}')",
     "C:\Program Files\VideoLAN\VLC\vlc.exe",],
    ["ctrl+h", "lambda: subprocess.call(program)", "notepad.exe"],
]

# Add the hotkeys
for hotkey in hotkeys:
    key, action, program = hotkey
    keyboard.add_hotkey(key, eval(action))

# Add the hotkeys
# for hotkey in hotkeys:
#    key, action, program = hotkey
#    keyboard.add_hotkey(key, eval(action))


def bg():
    for hotkeyy in hotkeys:
        key, action, program = hotkeyy
        print(hotkeyy)
        print(hotkeyy)


bg()

# define the edit function
# define the edit function


def edit_file(hotkeys):
    check_key = input("Change which key: ")
    for i, hotkey in enumerate(hotkeys):
        key, action, program, = hotkey
        if check_key == key:
            change_key = input(f"\033[34m{key}\033[0m {action} {program}")
            hotkeys[i][:] = (change_key, action, program, name, id)
            print(i)
            print(key)
            print(f"Key: {key}, Name: {action}, Book: {program}")
            print("hotkey")
            print(hotkeys[i])
            print(hotkeys)
            bg()
        elif check_key == action:
            change_key = input(f"\033[34m{key}\033[0m {action} {program}")
            hotkeys[i] = (key, change_key, program, name, id)
            print(f"Key: {key}, Name: {action}, Book: {program}")
        elif check_key == program:
            change_key = input(f"\033[34m{key}\033[0m {action} {program}")
            hotkeys[i] = (key, action, change_key, name, id)
            print(f"Key: {key}, Name: {action}, Book: {program}")


keyboard.wait()
