import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit
from PyQt5.QtCore import Qt, QObject, pyqtSlot

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the user interface
        self.button1 = QPushButton("Button 1", self)
        self.button1.move(10, 10)
        self.button1.clicked.connect(self.on_button1_clicked)

        self.button2 = QPushButton("Save", self)
        self.button2.move(10, 50)
        self.button2.clicked.connect(self.on_button2_clicked)

        self.text_edit = QTextEdit(self)
        self.text_edit.move(10, 90)
        self.text_edit.setReadOnly(True)

        # Set window properties
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Key Input")
        self.show()

    @pyqtSlot()
    def on_button1_clicked(self):
        # Wait for the user to press a key
        self.key = QObject.waitForKeyPress(self)
        # Display the key that was pressed in the text edit
        self.text_edit.setText(f"Key pressed: {self.key.key()}")

    @pyqtSlot()
    def on_button2_clicked(self):
        # Save the key that was pressed
        self.saved_key = self.key
        # Display the saved key in the text edit
        self.text_edit.setText(f"Saved key: {self.saved_key.key()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
