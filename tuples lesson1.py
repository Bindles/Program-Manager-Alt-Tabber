import keyboard

# define the hotkeys
keyboard.add_hotkey("ctrl+q", lambda: edit_file(hotkeys))

# Define the hotkeys
hotkeys = [
    ("ctrl+e", "lambda: keyboard.send(f'open {program}')", "C:\Program Files\Mozilla Firefox\firefox.exe", 1),
    ("ctrl+r", "lambda: keyboard.send(f'open {program}')", "C:\Program Files\VideoLAN\VLC\vlc.exe", 2)
]


# Display all hotkeys
for i, hotkey in enumerate(hotkeys):
    print(f"{i}: {hotkey}")

# Get user input of which part of the hotkey to change
index = int(input("Enter the index of the hotkey you want to change: "))
part = int(input("Enter the part of the hotkey you want to change (0-3): "))
value = input("Enter the new value: ")

# Modify the hotkey
hotkeys[index][part] = value

# Print the modified list of tuples
print(hotkeys)

            
keyboard.wait()

            

