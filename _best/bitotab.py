import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QComboBox, QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import ctypes
import keyboard

# Create a dict for hot key
build_hotkey = {"id": 1, "key": "key", "action": "action",
                "process_title": None, "process_hwnd": None}
# create a empty list for hot keys
hotkeys = []
process_name = ""
process_id = ""
# Create App
app = QApplication(sys.argv)
window = QDialog()
window.setWindowTitle('Hotkey Builder')
window.setWindowIcon(QIcon("icon.png"))
window.setGeometry(100, 100, 500, 500)
# Create a dropdown form with a default value of "Select Process"
select_process = QComboBox(window)
select_process.addItem("select Process")
# displaying a list of major process
processes = [
    {
        "process_title": "Notepad",
        "process_name": "notepad.exe",
        "hwnd": 8458
    },
    {
        "process_title": "Chrome",
        "process_name": "chrome.exe",
        "hwnd": 1298
    },
    {
        "process_title": "VSCode",
        "process_name": "code.exe",
        "hwnd": 4012
    },
]
for process in processes:
    item = "{} {} {}".format(
        process["process_title"], process["process_name"], process["hwnd"])
    select_process.addItem(item)
select_process.move(100, 100)


@pyqtSlot()
def select_process_func():
    idx = select_process.currentIndex()
    if idx == 0:
        # print("Select Process")
        window.l3.setText("Select Process")
    else:
        process = processes[idx-1]
        process_title = process['process_title']
        process_hwnd = process['hwnd']
        print("Process title:", process_title, "\nProcess hwnd:", process_hwnd)
        window.l3.setText(f"{process_title} {process_hwnd}")
        # window.l3.setText("Process title: {}\nProcess hwnd: {}".format(
        # process_title, process_hwnd))
        # modify the build_hotkey dict
        build_hotkey['process_title'] = process_title
        build_hotkey['process_hwnd'] = process_hwnd
        window.l1 = QLabel(window)
        window.l1.move(100, 200)
        window.l1.setText("{}".format(build_hotkey))
        rebuild_cur()


select_process.activated[str].connect(select_process_func)
# Create a Label to show contents of build_hotkey
# window.l1 = QLabel(window)
# window.l1.move(100, 200)
# window.l1.setText("{}".format(build_hotkey))


def rebuild_cur():
    print("hi")
    print(build_hotkey)
    # select_process.activated[str].connect(select_process_func)
    # Create a Label to show contents of build_hotkey
    window.l1 = QLabel(window)
    window.l1.move(100, 200)
    window.l1.setText("{}".format(build_hotkey))


# window.14 = Qlabel(window)
# window.14.move(130, 230)
# window.14.setText("[]".format(hotkeys))

# Create a label to show current process and hwnd selected
window.l3 = QLabel(window)
window.l3.move(100, 250)
window.l3.setText("No selection")
# Create a button to append new build_hotkey to hotkeys
btn_add_key = QPushButton("add Key", window)


def add_key():
    """    process_name = processes[process_name]
       process_id = processes[process_id] """
    build_hotkey['process_name'] = process_name
    build_hotkey['process_id'] = process_id
    hotkeys.append(build_hotkey)
    # Create a Label to show contents of hotkeys
    window.l2 = QLabel(window)
    window.l2.move(100, 350)
    window.l2.setText("{}".format(hotkeys))


btn_add_key.clicked.connect(add_key)
btn_add_key.setToolTip('Click to add selected hotkey to list of hotkeys')
# btn_add_key = QPushButton("add Key", window)
btn_add_key.clicked.connect(lambda: hotkeys.append(build_hotkey))
# btn_add_key.clicked.connect(lambda: hotkeys.append(build_hotkey))
btn_add_key.setToolTip('Click to add selected hotkey to list of hotkeys')
btn_add_key.resize(100, 30)
btn_add_key.move(100, 300)
# # Create a Label to show contents of hotkeys
# window.l2 = QLabel(window)
# window.l2.move(100, 350)
# window.l2.setText("{}".format(hotkeys))
# Create a button to press keys and modify key value of build_hotkey
# dict
key_press = QPushButton("Press Key", window)
# key_press.clicked.connect(lambda: build_hotkey['key']=keyboard.read_key())
key_press.setToolTip('Click to add selected hotkey to list of hotkeys')
key_press.resize(100, 30)
key_press.move(300, 300)
# Create a button to write hotkeys to a txt file in json format
btn_write_file = QPushButton("Write File", window)
btn_write_file.clicked.connect(lambda: open(
    'hotkeys.txt', 'w').write(json.dumps(hotkeys)))
btn_write_file.setToolTip('Click to write hotkeys to text file')
btn_write_file.resize(100, 30)
btn_write_file.move(200, 350)
# Show window
window.show()
sys.exit(app.exec_())
