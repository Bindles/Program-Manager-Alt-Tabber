import keyboard
import win32api
import win32con
import win32gui
import win32process
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QLineEdit, QPushButton

class Window(QWidget):
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
        """Returns a list of tuples containing the process ID and process name
        for all major programs that can be selected with alt + tab.
        """
        major_programs = []
        def enumHandler(hwnd, lParam):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
                try:
                    handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, pid)
                except:
                    return None
                process_name = win32process.GetModuleFileNameEx(handle, 0)
                major_programs.append((pid, process_name))
            return True

        win32gui.EnumWindows(enumHandler, None)
        return major_programs

    def processSelected(self):
        """Updates the text form with the currently selected process information."""
        index = self.process_dropdown.currentIndex()
        process_id = self.process_dropdown.itemData(index)
        process_name = self.process_dropdown.currentText().split(" ")[0]
        self.text_form.setText(f"Process ID: {process_id}\nProcess Name: {process_name}")


    def button1Clicked(self):
        """Waits for a key press and assigns it as the hotkey for the selected process."""
        hotkey = keyboard.read_hotkey()
        process_id = self.process_dropdown.currentData()
        process_name = self.process_dropdown.currentText().split(" ")[0]
        self.key1_hotkey_label.setText(f"Key 1 Hotkey: {hotkey}")
        self.key1_process_id_label.setText(f"Key 1 Process ID: {process_id}")
        self.key1_process_name_label.setText(f"Key 1 Process Name: {process_name}")
        # Register the hotkey with the keyboard library
        keyboard.add_hotkey(hotkey, self.key1Pressed)

    def key1Pressed(self):
        """Brings the process associated with key 1 to the front when the hotkey is pressed."""
        process_id = self.key1_process_id_label.text().split(": ")[1]
        handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, int(process_id))
        if handle:
            win32gui.ShowWindow(handle, win32con.SW_RESTORE)
            win32gui.SetForegroundWindow(handle)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    app.exec_()

