hotkeys = [
    ("ctrl+e", "lambda: keyboard.send(f'open {program}')", "C:\Program Files\Mozilla Firefox\firefox.exe", 1),
    ("ctrl+r", "lambda: keyboard.send(f'open {program}')", "C:\Program Files\VideoLAN\VLC\vlc.exe", 2)
]

# Get user input of which part of the hotkey to change
index = int(input("Enter the index of the hotkey you want to change: "))
part = int(input("Enter the part of the hotkey you want to change (0-3): "))
value = input("Enter the new value: ")

# Create a new tuple with the modified values
hotkey = hotkeys[index]
hotkey = hotkey[:part] + (value,) + hotkey[part+1:]

# Replace the old tuple with the new one
hotkeys[index] = hotkey

# Print the modified list of tuples
print(hotkeys)
