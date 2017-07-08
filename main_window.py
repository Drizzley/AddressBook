"""Class that creates the main window"""

from tkinter import *
from entry_window import EntryWindow

class MainWindow(object):

    def __init__(self):
        """Constructor"""
        self.root = Tk()

        self.left_frame = Frame(self.root)
        self.right_frame = Frame(self.root)
        
        self.add_new_button = Button(self.right_frame, text='Add New', command=self.open_entry_window)
        self.remove_button = Button(self.right_frame, text='Remove')
        self.close_button = Button(self.right_frame, text='Close', command=self.root.quit)

        self.left_frame.pack()
        self.right_frame.pack()
        self.add_new_button.pack()
        self.remove_button.pack()
        self.close_button.pack()

        self.root.mainloop()

    def open_entry_window(self):
        """Opens the EntryWindow object"""
        entry_window = EntryWindow()
