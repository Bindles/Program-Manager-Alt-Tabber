import tkinter as tk

hotkeys = [
    ["ctrl+e", "bring_to_front", "Untitled - Notepad", None],
    ["ctrl+r", "bring_to_front", "VLC media player", None]
]


class KeyPressApp:
    def __init__(self, master):
        self.master = master
        self.text_form = tk.Text(master, height=1, width=20)
        self.button = tk.Button(
            master, text="Press a key", command=self.key_press)

        self.text_form.pack()
        self.button.pack()

    def key_press(self):
        self.master.bind("<Key>", self.key_callback)

    def key_callback(self, event):
        keysym = event.keysym
        if event.state & 1:
            # Shift key is pressed
            keysym = "Shift+" + keysym
        elif event.state & 4:
            # Control key is pressed
            keysym = "Control+" + keysym
        elif event.state & 8:
            # Alt key is pressed
            keysym = "Alt+" + keysym
        self.text_form.delete('1.0', tk.END)
        self.text_form.insert(tk.END, keysym)


root = tk.Tk()
app = KeyPressApp(root)
root.mainloop()
