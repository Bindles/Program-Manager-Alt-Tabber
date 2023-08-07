hotkeys = [
     ["ctrl+e", "lambda: keyboard.send(f'open {program}')", "C:\Program Files\Mozilla Firefox\firefox.exe", 1],
     ["ctrl+r", "lambda: keyboard.send(f'open {program}')", "C:\Program Files\VideoLAN\VLC\vlc.exe", 2]
]

# Get user input of which part of the hotkey to change
index = int(input("Enter the index of the hotkey you want to change: "))
part = int(input("Enter the part of the hotkey you want to change (0-4): "))

if part == 0:
    # Get user input for the new list or tuple
    value = input("Enter the new values separated by commas: ")
    # Split the input into a list
    value = value.split(',')
    # Convert the elements to the correct type (if necessary)
    value = [int(x) if x.isdigit() else x for x in value]
else:
    # Get user input for the new value
    value = input("Enter the new value: ")
    # Convert the value to the correct type (if necessary)
    value = int(value) if value.isdigit() else value

# Modify the element of the list or tuple
hotkeys[index][part] = value

# Print the modified list or tuple
print(hotkeys[index])
