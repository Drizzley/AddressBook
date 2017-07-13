"""
The file that handles the Master's windows left frame.
All the results from the database will be shown here
"""

from tkinter import *

class LeftFrame(object):

    def __init__(self, root):
        self.frame = Frame(root)
        self.address_list = Listbox(self.frame)

        self.address_list.insert(END, 'Test 1')
        self.address_list.insert(END, 'Test 2')

        self.address_list.pack()
        self.frame.pack(side=LEFT)