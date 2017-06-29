"""Class that creates the main window"""

from tkinter import *

class MainWindow():

    def __init__(self, root, dataBase):
        """Constructor"""
        self.root = root
        self.dataBase = dataBase

        self.left_frame = Frame(root)
        self.right_frame = Frame(root)
        
        self.add_new_button = Button(right_frame, text='Add New')
        self.remove_button = Button(right_frame, text='Remove')
    