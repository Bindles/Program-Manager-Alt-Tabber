hotkeys = [
    ["ctrl+e", "lambda: keyboard.send(f'open {program}')",
     "C:\Program Files\Mozilla Firefox\firefox.exe", 1],
    ["ctrl+r", "lambda: keyboard.send(f'open {program}')",
     "C:\Program Files\VideoLAN\VLC\vlc.exe", 2]
]
# for i in hotkeys, enumerate:
# print(i, *hotkeys)
for i, hotkey in enumerate(hotkeys):
    print(i, *hotkey)

# print(hotkeys)
# Get the index of the list or tuple to modify
index = int(input("Enter the index of the list or tuple to modify (0-1): "))
# Get the part of the list or tuple to modify
part = int(input("Enter the part of the list or tuple to modify (0-3): ")) - 1

if part == -1:
    print("penis")
    print(hotkeys[index][:])
    # Get user input for the new list or tuple
    value = input("Enter the new values separated by commas: ")
    # Split the input into a list
    value = value.split(',')
    # Check the length and types of the values
    if len(value) != 4:
        # Print an error message if the length is not 4
        print("Error: Incorrect number of values")
    elif not all(map(lambda x: x.isdigit(), value[3:])):
        # Print an error message if the fourth value is not an integer
        print("Error: Fourth value must be an integer")
    else:
        # Convert the elements to the correct type (if necessary)
        value = [int(x) if x.isdigit() else x for x in value]
        # Use slicing to replace the elements of the list or tuple at index `index` with the new values
        print(hotkeys[index][:])
        print(">>>>")
        hotkeys[index][:] = value
else:
    # Get user input for the new value
    value = input(f"Enter the new value of {hotkeys[index][part]} : ")
    # Convert the element to the correct type (if necessary)
    value = int(value) if value.isdigit() else value
    # Modify the element of the list or tuple
    print(hotkeys[index][part])
    print(">>>>")
    print(value)
    hotkeys[index][part] = value

# Print the modified list or tuple
print(hotkeys[index])

# Print the entire list or tuple
print(hotkeys)
print(f"my name is {value}what is your {part} right?")
print(f"my name is jon what is your {part} right?")
