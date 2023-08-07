import sys
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QLabel, QPushButton
from ctypes import windll
import ctypes


class Hotkey(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.build_hotkey = {'id': 1, 'key': "key", 'action': "action",
                             'process_title': None, 'process_hwnd': None}
        self.hotkeys = []
        self.process_list = []
        self.process_title = None
        self.process_hwnd = None

    def get_process_list(self):
        EnumWindows = windll.user32.EnumWindows
        EnumWindowsProc = windll.user32.EnumWindowsProc
        GetWindowText = windll.user32.GetWindowTextW
        GetWindowTextLength = windll.user32.GetWindowTextLengthW
        IsWindowVisible = windll.user32.IsWindowVisible

        titles = []

        def foreach_window(hwnd, lParam):
            if IsWindowVisible(hwnd):
                length = GetWindowTextLength(hwnd)
                buff = ctypes.create_unicode_buffer(length + 1)
                GetWindowText(hwnd, buff, length + 1)
                titles.append((hwnd, buff.value))
            return True
        EnumWindows(EnumWindowsProc(foreach_window), 0)

        for hwnd, title in titles:
            self.process_list.append((hwnd, title))

    def update_process_title(self, process_title):
        self.build_hotkey['process_title'] = process_title
        for process in self.process_list:
            if process[1] == process_title:
                self.build_hotkey['process_hwnd'] = process[0]
                break

    def add_hotkey(self):
        self.hotkeys.append(self.build_hotkey)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.hotkey = Hotkey()
        self.hotkey.get_process_list()
        self.process_dropdown = QComboBox()
        self.process_dropdown.addItem("Select Process")
        for process in self.hotkey.process_list:
            self.process_dropdown.addItem(f'{process[1]}')
        self.process_dropdown.currentIndexChanged.connect(
            self.update_process_title)

        self.build_hotkey_label = QLabel()
        self.build_hotkey_label.setText(str(self.hotkey.build_hotkey))

        self.add_hotkey_button = QPushButton("Add Hotkey")
        self.add_hotkey_button.clicked.connect(self.add_hotkey)

        self.hotkeys_label = QLabel()
        self.update_hotkeys()

        layout = QVBoxLayout()
        layout.addWidget(self.process_dropdown)
        layout.addWidget(self.build_hotkey_label)
        layout.addWidget(self.add_hotkey_button)
        layout.addWidget(self.hotkeys_label)
        self.setLayout(layout)
        self.show()
        self.add_hotkey_button.clicked.connect(self.append_hotkey)

        def append_hotkey(self):
            self.hotkeys.append(self.build_hotkey)
            self.hotkeys_label.setText(str(self.hotkeys))

            # if __name__ == '__main__':
            # app = QApplication(sys.argv)
            # window = MainWindow()
            # sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
