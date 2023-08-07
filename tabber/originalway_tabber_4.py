import sys
import win32con
import win32api
import win32gui
import win32process

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QComboBox,
    QLineEdit,
    QPushButton,
    QLabel,
)

from PyQt5.QtCore import Qt, QEvent

import keyboard


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create the process dropdown
        self.process_dropdown = QComboBox(self)
        self.process_dropdown.move(10, 10)
        self.process_dropdown.addItem("Select a process")
        self.process_dropdown.currentIndexChanged.connect(self.processSelected)

        # Get the list of major programs that can be selected with alt + tab
        major_programs = self.getMajorPrograms()
        # Add the programs to the dropdown
        for process in major_programs:
            self.process_dropdown.addItem(f"{process.name} ({process.pid})", process.hwnd)

        # Create the text form
        self.text_form = QLineEdit(self)
        self.text_form.move(10, 50)

        # Create the button
        self.button1 = QPushButton('Button 1', self)
        self.button1.move(10, 90)
        self.button1.clicked.connect(self.button1Clicked)

        # Create the labels to display the hotkey and process information
        self.key1_hotkey_label = QLabel(self)
        self.key1_hotkey_label.move(10, 130)
        self.key1_process_id_label = QLabel(self)
        self.key1_process_id_label.move(10, 150)
        self.key1_process_name_label = QLabel(self)
        self.key1_process_name_label.move(10, 170)
        self.key1_process_hwnd_label = QLabel(self)
        self.key1_process_hwnd_label.move(10, 190)

        self.setGeometry(300, 300, 250, 200)
        self.setWindowTitle('Originalway Tabber')
        self.show()

    def getMajorPrograms(self):
        def enumHandler(handle, data):
            if win32process.GetWindowThreadProcessId(handle)[1] != 0:
                process_id = win32process.GetWindowThreadProcessId(handle)[1]
                process_name = win32process.GetWindowModuleFileName(handle)
                major_programs.append((process_id, process_name))

        major_programs = []
        win32gui.EnumWindows(enumHandler, None)
        return major_programs

    def processSelected(self, index):
        # Get the selected process information
        process_id = self.process_dropdown.itemData(index)
        process_name = self.process_dropdown.currentText().split(" (")[0]

        # Save the selected process information to the key1 variables
        self.key1_process_id = process_id
        self.key1_process_name = process_name
        self.key1_process_hwnd = win32gui.GetForegroundWindow()

        # Update the labels to display the selected process information
        self.key1_process_id_label.setText(f"Key 1 Process ID: {process_id}")
        self.key1_process_name_label.setText(f"Key 1 Process Name: {process_name}")
        self.key1_process_hwnd_label.setText(f"Key 1 Process hwnd: {self.key1_process_hwnd}")

    def button1Clicked(self):
        # Get the hotkey from the text form
        hotkey = self.text_form.text()

        # Set the hotkey for key 1
        keyboard.add_hotkey(hotkey, self.key1Pressed, suppress=True)

        # Save the hotkey to the key1 variable
        self.key1_hotkey = hotkey

        # Update the label to display the hotkey
        self.key1_hotkey_label.setText(f"Key 1 Hotkey: {hotkey}")

    def key1Pressed(self):
        # Open the process with the selected process id
        handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, self.key1_process_hwnd)
        win32gui.SetForegroundWindow(handle)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

