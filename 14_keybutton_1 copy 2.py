import sys
from PyQt5.QtWidgets import QApplication, QComboBox, QPushButton, QLabel, QVBoxLayout, QWidget
import keyboard


class HotkeySetter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create the dropdown form and add some dummy items
        self.process_combo = QComboBox(self)
        self.process_combo.addItems(["Process 1", "Process 2", "Process 3"])

        # Create the "Set Key" button and label
        self.bt_1 = QPushButton("Set Key", self)
        self.bt_1_label = QLabel(self)
        self.bt_1.clicked.connect(self.set_key)

        # Create the "Save" button
        self.bt_2 = QPushButton("Save", self)
        self.bt_2.clicked.connect(self.save_hotkey)

        # Create a vertical layout to hold the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.process_combo)
        layout.addWidget(self.bt_1)
        layout.addWidget(self.bt_1_label)
        layout.addWidget(self.bt_2)
        self.setLayout(layout)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Hotkey Setter")
        self.show()

    def set_key(self):
        self.bt_1_label.setText("Input Key...")
        self.pressed_key = keyboard.read_hotkey()
        self.bt_1_label.setText(self.pressed_key)

    def save_hotkey(self):
        self.hotkey1 = {
            "name": "key 1",
            "key": self.pressed_key,
            "process_name": self.process_com
