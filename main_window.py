"""Class that creates the main window"""

from tkinter import *
from entry_window import EntryWindow
from left_frame import LeftFrame

class MainWindow(object):

    def __init__(self):
        """Constructor"""
        self.root = Tk()
        self.root.wm_title('Address Book')

        self.left_frame = Frame(self.root)
        self.right_frame = Frame(self.root)
        
        self.add_new_button = Button(self.right_frame, text='Add New', command=self.open_entry_window)
        self.remove_button = Button(self.right_frame, text='Remove')
        self.close_button = Button(self.right_frame, text='Close', command=self.root.quit)
        
        self.address_list = Text(self.left_frame, width=30, height=20)
        self.address_list.insert(INSERT, 'Test 1')
        self.address_list.insert(END, 'Test 2')
        self.address_list.pack()

        self.left_frame.pack(side=LEFT)
        self.right_frame.pack()
        self.add_new_button.pack()
        self.remove_button.pack()
        self.close_button.pack()

        self.root.mainloop()

    def open_entry_window(self):
        """Opens the EntryWindow object"""
        entry_window = EntryWindow()

    def create_left_frame(self, root, frame):
        """Initializes all of the left frame components"""
        self.frame = Frame(root)

        self.address_list = Listbox(self.frame)

        self.address_list.insert(END, 'Test 1')
        self.address_list.insert(END, 'Test 2')

        self.address_list.pack()