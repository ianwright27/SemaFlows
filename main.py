from tkinter import Tk, Label, Button, StringVar, Frame, Menu


app = AppConfig()
LABEL_TEXT = [f"Welcome to {app.name}"]

root = Tk()
root.geometry('800x600')
gui = MainWindow(root)
root.mainloop()
# main window
