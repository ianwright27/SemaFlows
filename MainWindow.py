

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title(app.name)

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar, tearoff=False)
        fileMenu.add_command(label="New...", command=self.greet)
        fileMenu.add_command(label="Open...", command=self.greet)
        fileMenu.add_command(label="Save", command=self.greet)
        fileMenu.add_command(label="Save As", command=self.greet)
        fileMenu.add_command(label="Settings", command=self.greet)
        fileMenu.add_command(label="Close", command=master.quit)
        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.insert_separator(4)

        editMenu = Menu(menubar, tearoff=False)
        editMenu.add_command(label="Undo (Ctrl+Z)", command=self.greet)
        editMenu.add_command(label="Redo (Ctrl+Y)", command=self.greet)
        editMenu.add_command(label="Cut", command=self.greet)
        editMenu.add_command(label="Copy", command=self.greet)
        editMenu.add_command(label="Paste", command=self.greet)
        editMenu.add_command(label="Delete", command=self.greet)
        menubar.add_cascade(label="Edit", menu=editMenu)
        editMenu.insert_separator(2)

        viewMenu = Menu(menubar, tearoff=False)
        viewMenu.add_command(label="Zoom", command=self.greet)
        viewMenu.add_command(label="Tips", command=self.greet)
        viewMenu.add_command(label="Status Bar", command=self.greet)
        menubar.add_cascade(label="View", menu=viewMenu)

        helpMenu = Menu(menubar, tearoff=False)
        helpMenu.add_command(label="View Help", command=self.greet)
        helpMenu.add_command(label="Send Feedback", command=self.greet)
        helpMenu.add_command(label="Learn More", command=self.greet)
        helpMenu.add_command(label="Check for Updates...", command=self.greet)
        helpMenu.add_command(label="About SemaFlows", command=self.greet)
        menubar.add_cascade(label="Help", menu=helpMenu)
        helpMenu.insert_separator(3)

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.pack()

        # self.greet_button = Button(master, text="Greet", command=self.greet)
        # self.greet_button.pack()
        #
        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.pack()

    def greet(self):
        print("Test!")

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(LABEL_TEXT) # wrap around
        self.label_text.set(LABEL_TEXT[self.label_index])


class AppConfig:
    def __init__(self):
        self.name = "SemaFlows"
        self.description = "Semantic Networks Design Tool"
        self.features = []

