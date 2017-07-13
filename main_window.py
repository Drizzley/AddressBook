"""Class that creates the main window"""

from tkinter import *
from entry_window import EntryWindow
from left_frame import LeftFrame

class MainWindow(object):

    def __init__(self):
        """Constructor"""
        self.root = Tk()
        self.root.wm_title('Address Book')

        self.left_frame = self.create_left_frame()#Frame(self.root)
        self.right_frame = Frame(self.root)
        
        self.add_new_button = Button(self.right_frame, text='Add New', command=self.open_entry_window)
        self.remove_button = Button(self.right_frame, text='Remove')
        self.close_button = Button(self.right_frame, text='Close', command=self.root.quit)

        self.right_frame.pack()
        self.add_new_button.pack()
        self.remove_button.pack()
        self.close_button.pack()

        self.root.mainloop()

    def open_entry_window(self):
        """Opens the EntryWindow object"""
        entry_window = EntryWindow()

    def create_left_frame(self):
        """Initializes all of the left frame components"""
        left_frame = LeftFrame(self.root)
        return left_frame

