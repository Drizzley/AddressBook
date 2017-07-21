"""Class that creates the main window"""

from tkinter import *
from entry_window import EntryWindow
from left_frame import LeftFrame
from right_frame import RightFrame

class MainWindow(object):

    def __init__(self):
        """Constructor"""
        self.root = Tk()
        self.root.wm_title('Address Book')

        self.left_frame = self.create_left_frame()
        self.right_frame = self.create_right_frame()
        
        self.root.mainloop()

    def create_left_frame(self):
        """Initializes all of the left frame components"""
        left_frame = LeftFrame(self.root)
        return left_frame

    def create_right_frame(self):
        right_frame = RightFrame(self.root)
        return right_frame
