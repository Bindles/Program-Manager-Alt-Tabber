import ctypes
import subprocess
import keyboard

# define the hotkeys
keyboard.add_hotkey("ctrl+q", lambda: edit_file(hotkeys))

# Define the hotkeys
hotkeys = [
    ("ctrl+e", "lambda: keyboard.send(f'open {program}')", "C:\Program Files\Mozilla Firefox\firefox.exe", 1),
    ("ctrl+r", "lambda: keyboard.send(f'open {program}')", "C:\Program Files\VideoLAN\VLC\vlc.exe", 2)
]

# Add the hotkeys
#for hotkey in hotkeys:
#    key, action, program = hotkey
#    keyboard.add_hotkey(key, eval(action))
for hotkeyy in hotkeys:
    key, action, program, id= hotkeyy
    print(hotkeyy)
    #print(hotkeys[1] * 7)


# define the edit function
def edit_file(hotkeys):
    check_key = input("Change which key: ")
    for hotkey in hotkeys:
        key, action, program, id = hotkey
        if check_key == key:
            change_key = input(f"\033[34m{key}\033[0m {action} {program}")
            hotkeys[hotkeys.index(hotkey)] = (change_key, action, program)
            print (type(hotkey))
            print(f"Key: {key}, Name: {action}, Book: {program}")
        elif check_key == action:
            change_key = input(f"\033[34m{key}\033[0m {action} {program}")
            hotkey = (key, change_key, program)
            print(f"Key: {key}, Name: {action}, Book: {program}")
        elif check_key == program:
            change_key = input(f"\033[34m{key}\033[0m {action} {program}")
            hotkey = (key, action, change_key)
            print(f"Key: {key}, Name: {action}, Book: {program}")
            
            
keyboard.wait()

            

