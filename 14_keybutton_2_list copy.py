import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.waiting_for_key = False
        self.key_1 = None

    def init_ui(self):
        # Create bt_1 and its label
        self.bt_1 = QPushButton("Set Key", self)
        self.bt_1_label = QLabel("", self)
        self.bt_1.clicked.connect(self.on_bt_1_clicked)
        self.bt_1.move(10, 10)
        self.bt_1_label.move(10, 50)

        # Create bt_2 and its label
        self.bt_2 = QPushButton("Save", self)
        self.bt_2_label = QLabel("", self)
        self.bt_2.clicked.connect(self.on_bt_2_clicked)
        self.bt_2.move(10, 90)
        self.bt_2_label.move(10, 130)

        self.setGeometry(166, 166, 122, 170)
        self.setWindowTitle("KeyMan")

    def on_bt_1_clicked(self):
        self.waiting_for_key = True
        self.bt_1_label.setText("Input Key...")
        self.bt_1_label.adjustSize()

    def on_bt_2_clicked(self):
        if self.key_1:
            hotkey_dict = {
                "name": "key 1",
                "key": self.key_1,
                "process": "process id",
            }
            self.bt_2_label.setText(
                f"{hotkey_dict['name']}: {hotkey_dict['key']} {hotkey_dict['process']}")
            self.bt_2_label.adjustSize()

    def keyPressEvent(self, event):
        if self.waiting_for_key:
            # Save the key press and update the label
            self.key_1 = event.text()
            self.bt_1_label.setText(self.key_1)
            self.bt_1_label.adjustSize()
            self.waiting_for_key = False


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
