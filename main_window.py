"""Class that creates the main window"""

from tkinter import *

class MainWindow():

    def __init__(self, root):
        """Constructor"""
        self.root = root

        self.left_frame = Frame(self.root)
        self.right_frame = Frame(self.root)
        
        self.add_new_button = Button(self.right_frame, text='Add New')
        self.remove_button = Button(self.right_frame, text='Remove')

        self.left_frame.pack()
        self.right_frame.pack()
        self.add_new_button.pack()
        self.remove_button.pack()

        self.root.mainloop()
    