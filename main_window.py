"""Class that creates the main window"""

from tkinter import *
from entry_window import EntryWindow
from left_frame import LeftFrame
from right_frame import RightFrame
from database_class import DataBaseClass

class MainWindow(object):

    def __init__(self):
        """Constructor"""
        self.root = Tk()
        self.root.geometry('300x200')
        self.root.wm_title('Address Book')

        self.database = DataBaseClass()

        self.left_frame = LeftFrame(self.root, self.database)
        self.right_frame = RightFrame(self.root, self.left_frame, self.database)
        
        self.root.mainloop()
        
