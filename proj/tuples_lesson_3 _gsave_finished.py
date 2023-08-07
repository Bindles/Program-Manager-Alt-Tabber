import configparser
import os

# Function to save the hotkeys list to a file


def save(hotkeys):
    config = configparser.ConfigParser()
    config['HOTKEYS'] = {}
    for i, hotkey in enumerate(hotkeys):
        config['HOTKEYS'][f'hotkey{i}'] = ','.join(hotkey)
        # config['HOTKEYS'][f'hotkey{i}'] = ','.join([str(x) for x in hotkey])  # save after converting all to string
        # config['HOTKEYS'][f'hotkey{i}'] = ','.join(hotkey[:3]) #save only 3 elements
    with open('test01.ini', 'w') as configfile:
        config.write(configfile)

# Function to load the hotkeys list from a file


def load():
    config = configparser.ConfigParser()
    config.read('test01.ini')
    hotkeys = []
    for key in config['HOTKEYS']:
        hotkeys.append(config['HOTKEYS'][key].split(','))
    return hotkeys


# Initialize the hotkeys list
if os.path.exists('test01.ini'):
    hotkeys = load()
else:
    hotkeys = [
        ["ctrl+e", "lambda: keyboard.send(f'open {program}')",
         "C:\Program Files\Mozilla Firefox\firefox.exe"],
        ["ctrl+r", "lambda: keyboard.send(f'open {program}')",
         "C:\Program Files\VideoLAN\VLC\vlc.exe"]
    ]

# Print the hotkeys list
print(hotkeys)
# Get the index of the list or tuple to modify
index = int(input("Enter the index of the list or tuple to modify (0-1): "))-1
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
    print(value)

# Print the modified list or tuple
print(hotkeys[index])
save(hotkeys)

# Print the entire list or tuple
print(value)
print(hotkeys)
print(f"my name is {value}what is your {part} right?")
print(f"my name is jon what is your {part} right?")
