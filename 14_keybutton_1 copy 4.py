import ctypes
import keyboard
from PyQt5 import QtWidgets, QtGui


class HotkeySetter(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create the process combo box
        self.process_combo = QtWidgets.QComboBox(self)
        self.process_combo.addItems(self.get_processes())

        # Create the Set Key button
        self.bt_1 = QtWidgets.QPushButton('Set Key', self)
        self.bt_1.clicked.connect(self.set_key)
        self.bt_1_label = QtWidgets.QLabel(self)

        # Create the Save button
        self.bt_2 = QtWidgets.QPushButton('Save', self)
        self.bt_2.clicked.connect(self.save_hotkey)

        # Create the layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.process_combo)
        layout.addWidget(self.bt_1)
        layout.addWidget(self.bt_1_label)
        layout.addWidget(self.bt_2)

        self.setLayout(layout)

    def set_key(self):
        # Wait for a key press
        self.pressed_key = keyboard.read_hotkey()
        # Update the label and button text
        self.bt_1_label.setText(self.pressed_key)
        self.bt_1.setText('Input Key...')

    def save_hotkey(self):
        # Create a hotkey dict and add it to the hotkeys list
        hotkey = {
            'name': 'key 1',
            'key': self.pressed_key,
            'process_name': self.process_combo.currentText(),
            'process_hwnd': self.process_combo.currentData()
        }
        hotkeys.append(hotkey)
        print(hotkeys)

    def get_processes(self):
        # Get a list of all top level windows
        windows = ctypes.windll.user32.GetTopWindow(None)
        processes = []
        # Iterate through the windows and get their names
        while windows:
