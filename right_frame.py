"""Class for the right frame"""

from tkinter import *
from entry_window import EntryWindow

class RightFrame(object):

    def __init__(self, root):
        self.frame = Frame(root)

        self.add_new_button = Button(self.frame, text='Add New', command=self.open_entry_window)
        self.remove_button = Button(self.frame, text='Remove')
        self.close_button = Button(self.frame, text='Close', command=root.quit)

        self.add_new_button.pack()
        self.remove_button.pack()
        self.close_button.pack()
        self.frame.pack()

    def open_entry_window(self):
        """Opens the EntryWindow object"""
        entry_window = EntryWindow()
