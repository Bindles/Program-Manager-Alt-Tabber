import sys
import subprocess
import keyboard
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QKeySequence

class KeyInputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Create a button and a text field
        self.button = QPushButton('Press a key', self)
        self.text_field = QLineEdit(self)

        # Connect the button to the keyInput function
        self.button.clicked.connect(self.keyInput)

        # Show the window
        self.show()

    def keyInput(self):
        # Wait for the user to press a key
        self.text_field.grabKeyboard()
        self.text_field.keyPressEvent = self.saveKey

    def saveKey(self, event):
        # Save the key press as a variable
        self.key = QKeySequence(event.modifiers() + event.key()).toString()

        # Release the keyboard and close the window
        self.text_field.releaseKeyboard()
        self.close()

def bringNotepadToFront():
    # Bring the Notepad application to the front
    subprocess.call(['wmctrl', '-a', 'notepad.exe'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KeyInputWindow()
    sys.exit(app.exec_())
    
    # Add the keyboard shortcut
    keyboard.add_hotkey(window.key, bringNotepadToFront)
    
    # Start listening for keyboard events
    keyboard.wait()
