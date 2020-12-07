from tkinter import Tk, Label, Button, StringVar, Frame, Menu
# modules
from MainWindow import * # main features


app = AppConfig()

root = Tk()
root.geometry('800x600')
gui = MainWindow(root)
root.mainloop()
# main window
