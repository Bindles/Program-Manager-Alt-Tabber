import ctypes
import keyboard
from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QPushButton, QVBoxLayout, QWidget


class HotkeySetter(QWidget):
    def __init__(self):
        super().__init__()
        self.hotkey = {}
        self.init_ui()

    def init_ui(self):
        # Create the dropdown list of processes
        self.process_combo = QComboBox(self)
        self.process_combo.addItems(self.get_processes())

        # Create the "Set Key" button
        self.key_label = QLabel("Press a key to set as hotkey", self)
        self.set_key_button = QPushButton("Set Key", self)
        self.set_key_button.clicked.connect(self.set_key)

        # Create the "Save" button
        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_hotkey)

        # Create the layout and add the widgets
        layout = QVBoxLayout(self)
        layout.addWidget(self.process_combo)
        layout.addWidget(self.key_label)
        layout.addWidget(self.set_key_button)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
        self.setWindowTitle("Hotkey Setter")
        self.show()

    def get_processes(self):
        # Get a list of major running processes
        processes = []
        window = ctypes.windll.user32.GetForegroundWindow()
        processes.append(ctypes.windll.user32.GetWindowText(window))
        hwnd = ctypes.windll.user32.GetWindow(window, 2)
        while hwnd != 0:
            processes.append(ctypes.windll.user32.GetWindowText(hwnd))
            hwnd = ctypes.windll.user32.GetWindow(hwnd, 2)
        return processes

    def set_key(self):
        # Wait for a key press and update the key label
        self.hotkey["key"] = keyboard.read_hotkey()
        self.key_label.setText(self.hotkey["key"])

    def save_hotkey(self):
        # Save the hotkey to the dictionary
        self.hotkey["process_name"] = self.process_combo.currentText()
        self.hotkey["process_hwnd"] = ctypes.windll.user32.FindWindowW(
            None, self.hotkey["process_name"])
        print(self.hotkey)


if __name__ == "__main__":
    app = QApplication([])
    hotkey_setter = HotkeySetter()
    app.exec_()
