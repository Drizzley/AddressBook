"""Class for the right frame"""

from tkinter import *
from entry_window import EntryWindow

class RightFrame(object):

    def __init__(self, root, left_frame, database):
        self.frame = Frame(root)
        self.left_frame = left_frame
        self.database = database

        self.add_new_button = Button(self.frame, text='Add New', command=self.open_entry_window)
        self.export_button = Button(self.frame, text='Export', command=self.splitNameSelection)
        self.remove_button = Button(self.frame, text='Remove')
        self.close_button = Button(self.frame, text='Close', command=root.quit)

        self.add_new_button.pack()
        self.export_button.pack()
        self.remove_button.pack()
        self.close_button.pack()
        self.frame.pack()

    def open_entry_window(self):
        """Opens the EntryWindow object"""
        entry_window = EntryWindow()

    def getListboxFromFrame(self):
        frame_children = self.left_frame.frame.winfo_children()
        list_box = frame_children[0]
        return list_box

    def getListBoxSelection(self):
        list_box = self.getListboxFromFrame()
        return list_box.get(ACTIVE)

    def splitNameSelection(self):
        name = self.getListBoxSelection()
        name_list = name.split(' ')
        name_dict = {
            'first_name': name_list[0],
            'last_name': name_list[1]
        }
        return name_dict

    
