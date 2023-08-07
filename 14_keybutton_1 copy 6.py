from PyQt5.QtWidgets import QApplication, QComboBox, QGridLayout, QPushButton, QLabel, QWidget
from PyQt5.QtCore import Qt
import keyboard
import ctypes
import sys


class HotkeySetter(QWidget):
    def init(self):
        super().init()
        self.init_ui()
        self.show()


def init_ui(self):
    self.setGeometry(100, 100, 400, 100)
    self.setWindowTitle("Hotkey Setter")
    self.setWindowFlags(Qt.WindowStaysOnTopHint)

    grid = QGridLayout()
    self.setLayout(grid)

    self.process_combo = QComboBox()
    self.process_combo.addItems(self.get_processes())
    grid.addWidget(self.process_combo, 0, 0)

    bt_1 = QPushButton("Set Key")
    bt_1.clicked.connect(self.set_hotkey)
    bt_1_label = QLabel("")
    grid.addWidget(bt_1, 0, 1)
    grid.addWidget(bt_1_label, 0, 2)

    bt_2 = QPushButton("Save")
    bt_2.clicked.connect(self.save_hotkey)
    grid.addWidget(bt_2, 1, 0)

    self.bt_1_label = bt_1_label
    self.bt_1 = bt_1


def set_hotkey(self):
    self.bt_1.setText("Input Key...")
    self.bt_1_label.setText("")
    keyboard.wait()
    self.pressed_key = keyboard.read_event()[1]
    self.bt_1.setText(self.pressed_key)
    self.bt_1_label.setText(self.pressed_key)


def save_hotkey(self):
    hotkey = {
        "name": "key 1",
        "key": self.pressed_key,
        "process_name": self.process_combo.currentText(),
        "process_hwnd": self.processes[self.process_combo.currentIndex()][1]
    }
    self.hotkeys.append(hotkey)
    print(self.hotkeys)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    hotkey_setter = HotkeySetter()
    sys.exit(app.exec_())
