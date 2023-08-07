hotkeys = [
     ["ctrl+e", "lambda: keyboard.send(f'open {program}')", "C:\Program Files\Mozilla Firefox\firefox.exe", 1],
     ["ctrl+r", "lambda: keyboard.send(f'open {program}')", "C:\Program Files\VideoLAN\VLC\vlc.exe", 2]
]

# Get user input of which part of the hotkey to change
index = int(input("Enter the index of the hotkey you want to change: "))
part = int(input("Enter the part of the hotkey you want to change (0-3): "))
value = input("Enter the new value: ")

# Modify the element of the list
hotkeys[index][part] = value

# Print the modified list of lists
print(hotkeys)
