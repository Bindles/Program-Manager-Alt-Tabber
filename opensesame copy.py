import keyboard
import os
import time

PROGRAM_1 = ""

# Check for start.ini file and set PROGRAM_1
if os.path.exists("start.ini"):
    with open("start.ini") as f:
        PROGRAM_1 = f.read()

# Display instructions
print("Hide: [ctrl][z] Close: [ctrl][x] Open [ctrl][c] Edit [ctrl][a]")

while True:
    try:
        # Wait for a key press
        keyboard.wait()

        # Check for specific key combinations
        if keyboard.is_pressed("ctrl+x"):
            # Close the program
            break
        elif keyboard.is_pressed("ctrl+z"):
            # Hide the program
            time.sleep(0.1)  # small delay to prevent double tap
            os.system("taskkill /im python.exe /f")
        elif keyboard.is_pressed("ctrl+c"):
            # Open program_1
            os.system(f"start {PROGRAM_1}")
        elif keyboard.is_pressed("ctrl+a"):
            # Edit start.ini file
            os.system("notepad start.ini")
    except KeyboardInterrupt:
        # Exit program when ctrl+c is pressed
        print("Keyboard interrupt received, exiting program")
        break

# Exit program
print("Exiting program")
