"""
The file that handles the Master's windows left frame.
All the results from the database will be shown here
"""

from tkinter import *
import MySQLdb

class LeftFrame(object):

    def __init__(self, root, database):
        self.frame = Frame(root)
        self.database = database
        self.address_list = Listbox(self.frame)

        self.db = MySQLdb.connect(
            host = 'localhost',
            user = 'testuser',
            passwd = 'testpassword',
            db = 'testdb'
        )

        self.populateContactList()

        self.address_list.pack(fill=BOTH, expand=1)
        self.frame.pack(side=LEFT, fill=BOTH)

    def populateContactList(self):
        person_list = self.database.getNamesOfCustomers()

        if self.address_list.size():
            self.address_list.delete(0, END)
            
        for name in person_list:
            self.address_list.insert(END, name)
