import sys
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QTextEdit
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Hotkey Program Selector')

        # Create combo box to select program
        global combo_box
        combo_box = QComboBox(self)
        combo_box.addItem('Select Program')

        # Get list of running processes and their information
        processes = psutil.process_iter()
        excluded_processes = ['System', 'Idle', 'System Idle Process']
        processes = [p for p in processes if p.name() not in excluded_processes]
        for process in processes:
            process_info = process.as_dict(attrs=['pid', 'name'])
            combo_box.addItem(f'{process_info["pid"]} - {process_info["name"]}')

        combo_box.move(50, 50)
        combo_box.setFixedWidth(200)

        # Create text edit to display selected process information
        global text_edit
        text_edit = QTextEdit(self)
        text_edit.setReadOnly(True)
        text_edit.move(50, 100)
        text_edit.setText('Process ID: \nProcess Name: \nHotkey: ')
        text_edit.setFixedWidth(200)

        # Create button to assign hotkey
        global button
        button = QPushButton('Assign Hotkey', self)
        button.move(50, 150)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
