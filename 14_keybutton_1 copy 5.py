import sys
import ctypes
import keyboard
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class HotkeySetter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # create a dropdown list of all running processes
        self.process_combo = QComboBox(self)
        self.process_combo.addItems(self.get_processes())

        # create the Set Key button and label
        self.bt_1_label = QLabel("Set Key", self)
        self.bt_1 = QPushButton("Set Key", self)
        self.bt_1.clicked.connect(self.get_key)

        # create the Save button
        self.bt_2 = QPushButton("Save", self)
        self.bt_2.clicked.connect(self.save_hotkey)

        # create the layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.process_combo)
        layout.addWidget(self.bt_1_label)
        layout.addWidget(self.bt_1)
        layout.addWidget(self.bt_2)

        # set the window properties
        self.setWindowTitle("Hotkey Setter")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def get_processes(self):
        # get a list of all windows
        windows = ctypes.windll.user32.EnumWindows(None, 0)

        # iterate through the windows and get their titles
        processes = []
        for window in windows:
            processes.append(ctypes.windll.user32.GetWindowText(window))

        return processes

    def get_key(self):
        # change the text to "Input Key..."
        self.bt_1_label.setText("Input Key...")

        # wait for a key press
        key = keyboard.read_hotkey()

        # update the label with the key press
        self.bt_1_label.setText(key)

    def save_hotkey(self):
        # Create a hotkey dictionary and add it to the hotkeys list
        hotkey = {"name": "key 1", "key": self.pressed_key, "process_name": self.process_combo.currentText(
        ), "process_hwnd": self.processes[self.process_combo.currentIndex()][1]}
        self.hotkeys.append(hotkey)
        self.key_label.setText(f"Saved Hotkey: {hotkey['key']}")
        self.bt_1_label.setText("Set Key")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    hotkey_setter = HotkeySetter()
    sys.exit(app.exec_())
