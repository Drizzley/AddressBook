"""
The file that handles the Master's windows left frame.
All the results from the database will be shown here
"""

from tkinter import *
import MySQLdb

class LeftFrame(object):

    def __init__(self, root):
        self.frame = Frame(root)
        self.address_list = Listbox(self.frame)

        self.db = MySQLdb.connect(
            host = 'localhost',
            user = 'testuser',
            passwd = 'testpassword',
            db = 'testdb'
        )

        #self.address_list.insert(END, 'Alberto')
        #self.address_list.insert(END, 'Mia')
        self.populateContactList()

        self.address_list.pack()
        self.frame.pack(side=LEFT)

    def populateContactList(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT first_name, last_name FROM foodtown')
        results = cursor.fetchall()
        if results:
            for person in results:
                name = person[0] + ' ' + person[1]
                self.address_list.insert(END, name)
