import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QLabel, QLineEdit
import win32gui
import win32api
import win32con
import keyboard
import win32process

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.selected_process_id = None
        self.selected_process_name = None
        self.key1_hotkey = None
        self.key1_process_id = None
        self.key1_process_name = None
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
        for process_id, process_name in major_programs:
            self.process_dropdown.addItem(f"{process_name} ({process_id})", process_id)

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

        self.setGeometry(300, 300, 250, 200)
        self.setWindowTitle('Originalway Tabber')
        self.show()

    def getMajorPrograms(self):
        def enumHandler(hwnd, lParam):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
                try:
                    handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, pid)
                    process_name = win32process.GetModuleFileNameEx(handle, 0)
                    if "\\" in process_name:
                        process_name = process_name.split("\\")[-1]
                    major_programs.append((pid, process_name))
                except:
                    pass

        major_programs = []
        win32gui.EnumWindows(enumHandler, None)
        return major_programs

    def processSelected(self):
        index = self.process_dropdown.currentIndex()
        self.selected_process_id = self.process_dropdown.itemData(index)
        self.selected_process_name = self.process_dropdown.currentText()

    def button1Clicked(self):
        if not self.selected_process_id:
            return
        hotkey = keyboard.read_hotkey()
        process_id = self.selected_process_id
        process_name = self.selected_process_name
        self.key1_hotkey = hotkey
        self.key1_process_id = process_id
        self.key1_process_name = process_name
        self.key1_hotkey_label.setText(f"Key 1 Hotkey: {self.key1_hotkey}")
        self.key1_process_id_label.setText(f"Key 1 Process ID: {self.key1_process_id}")
        self.key1_process_name_label.setText(f"Key 1 Process Name: {self.key1_process_name}")
        keyboard.add_hotkey(hotkey, self.key1Pressed)

    def key1Pressed(self):
        handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, self.key1_process_id)
        win32gui.SetForegroundWindow(handle)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
