import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # create a button and a label
        self.button = QPushButton("Set Shortcut Key", self)
        self.label = QLabel(self)
        
        # set the button and label positions
        self.button.move(50, 50)
        self.label.move(50, 100)
        
        # connect the button's clicked signal to the setKey function
        self.button.clicked.connect(self.setKey)
        
        # set the window properties
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Shortcut Key Demo")
        self.show()
        
    def setKey(self):
        # disable the button to prevent multiple key press events from being caught
        self.button.setEnabled(False)
        
        # set the label text to indicate that the user should press a key
        self.label.setText("Press a key...")
        
    def keyPressEvent(self, event):
        # get the keyboard modifiers and key that were pressed
        modifiers = event.modifiers()
        key = event.key()
        
        # generate the string representation of the shortcut
        mod_strings = []
        if modifiers & Qt.ControlModifier:
            mod_strings.append("Ctrl")
        if modifiers & Qt.AltModifier:
            mod_strings.append("Alt")
        if modifiers & Qt.ShiftModifier:
            mod_strings.append("Shift")
        if modifiers & Qt.MetaModifier:
            mod_strings.append("Meta")
        key_string = QKeySequence.StandardKey.keyToString(key)
        
        # create a QKeySequence object for the shortcut
        shortcut = QKeySequence.fromString("+".join(mod_strings + [key_string]))
        
        # save the shortcut for future use
        self.shortcut = shortcut
        
        # convert the shortcut to a string representation
        key_string = shortcut.toString()
        
        # display the shortcut key in the label
        self.label.setText("Shortcut Key: {}".format(key_string))
        
        # re-enable the button
        self.button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
