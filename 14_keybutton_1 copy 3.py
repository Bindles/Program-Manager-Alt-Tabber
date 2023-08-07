import sys
import keyboard
from PyQt5.QtWidgets import QApplication, QComboBox, QFormLayout, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QKeySequence


class HotkeySetter(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the UI
        self.init_ui()

    def init_ui(self):
        # Create the layout
        layout = QVBoxLayout()

        # Create the process combo box
        self.process_combo = QComboBox()
        self.process_combo.addItems(self.get_processes())

        # Create the label for the key
        self.key_label = QLabel("Press a key to set")

        # Create the set key button
        self.set_key_button = QPushButton("Set Key")
        self.set_key_button.clicked.connect(self.set_key)

        # Create the save button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_hotkey)

        # Add the widgets to the layout
        layout.addWidget(self.process_combo)
        layout.addWidget(self.key_label)
        layout.addWidget(self.set_key_button)
        layout.addWidget(self.save_button)

        # Set the layout
        self.setLayout(layout)

        # Show the widget
        self.show()

    def get_processes(self):
        """Get a list of running processes that are able to be alt-tabbed into"""
        processes = []

        # Enumerate all windows
        def callback(window, _):
            # Get the window title
            processes.append(ctypes.windll.user32.GetWindowText(window))
            return True

        ctypes.windll.user32.EnumWindows(callback, 0)

        # Return the list of processes
        return processes

    def set_key(self):
        """
