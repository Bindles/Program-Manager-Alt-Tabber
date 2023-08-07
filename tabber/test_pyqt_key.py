import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit
from PyQt5.QtCore import Qt, QEvent


class KeyPressWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a button and a text form
        self.button = QPushButton('Press a key', self)
        self.text_form = QTextEdit(self)

        # Set the button and text form positions
        self.button.move(20, 20)
        self.text_form.move(20, 60)

        # Set the button size
        self.button.resize(self.button.sizeHint())

        # Connect the button's clicked signal to the on_button_clicked slot
        self.button.clicked.connect(self.on_button_clicked)

        # Set the widget's size and title, and show it
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Key press')
        self.show()

    def on_button_clicked(self):
        # Clear the text form
        self.text_form.clear()

        # Set the widget to grab key events
        self.grabKeyboard()

        # Wait for a key press event
        key_event = self.wait_for_key_event()

        # Release the keyboard grab
        self.releaseKeyboard()

        # Get the key or key combination being pressed
        key_text = self.get_key_text(key_event)

        # Display the key or key combination in the text form
        self.text_form.append(key_text)

    def wait_for_key_event(self):
        # Wait for a key press event
        while True:
            QApplication.processEvents()
            event = self.key_event
            if event:
                return event



    def get_key_text(self, key_event):
        # Get the key being pressed
        key = key_event.key()

        # Get the text associated with the key
        key_text = key_event.text()

        # Check if the key is a combination of multiple keys
        if key == Qt.Key_unknown:
            # Get the key combination as a string
            key_combination = key_event.modifiers()
            key_text = f'Key combination: {key_combination}'
        else:
            # Get the key as a string
            key_text = f'Key: {key_text} ({key})'

        return key_text
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    key_press_widget = KeyPressWidget()
    sys.exit(app.exec_())
