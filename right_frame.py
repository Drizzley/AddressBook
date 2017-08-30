"""Class for the right frame"""

from tkinter import *
from entry_window import EntryWindow
from export_window import ExportWindow

class RightFrame(object):

    def __init__(self, root, left_frame, database):
        self.frame = Frame(root)
        self.left_frame = left_frame
        self.database = database

        self.add_new_button = Button(self.frame, text='Add New', command=self.open_entry_window)
        self.mia = Button(self.frame, text='Edit', command=self.editEntry)
        self.export_button = Button(self.frame, text='Export', command=self.openExportWindow)
        self.remove_button = Button(self.frame, text='Remove', command=self.removeCustomer)
        self.close_button = Button(self.frame, text='Close', command=root.quit)

        self.add_new_button.pack(fill=X)
        self.mia.pack(fill=X)
        self.export_button.pack(fill=X)
        self.remove_button.pack(fill=X)
        self.close_button.pack(fill=X)
        self.frame.pack(fill=BOTH)

    def open_entry_window(self):
        """Opens the EntryWindow object"""
        entry_window = EntryWindow(self.database, self.left_frame)

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

    def getAddressFromName(self):
        name_dict = self.splitNameSelection()
        self.database.returnAddressFromName(name_dict)

    def getAllInfo(self):
        name_dict = self.splitNameSelection()
        self.database.returnAllCustomerInfo(name_dict)

    def createCustomerDictionary(self):
        """Creates a dictionary with customer info
           from database"""
        name_dict = self.splitNameSelection()
        customer_info_list = self.database.returnAllCustomerInfo(name_dict)
        customer_name = customer_info_list[1] + ' ' + customer_info_list[2] + ' (' + customer_info_list[8] + ')'
        city_state_zip = customer_info_list[6] + ', ' + customer_info_list[5] + ' ' + customer_info_list[7]
        customer_info_dict = {
            'full_name': customer_name,
            'address_1': customer_info_list[3],
            'address_2': customer_info_list[4],
            'address_3': city_state_zip
        }
        return customer_info_dict

    def openExportWindow(self):
        customer_dict = self.createCustomerDictionary()
        export_window = ExportWindow(customer_dict)

    def removeCustomer(self):
        name_dict = self.splitNameSelection()
        self.database.deleteCustomerFromDB(name_dict)
        self.left_frame.populateContactList()

    def editEntry(self):
        name_dict = self.splitNameSelection()
        customer_info_dict = self.database.returnAllCustomerInfo(name_dict)
        #print(customer_info_dict)
        cust = {
            'first_name': customer_info_dict[1],
            'last_name': customer_info_dict[2],
            'address1': customer_info_dict[3],
            'address2': customer_info_dict[4],
            'state': customer_info_dict[5],
            'city': customer_info_dict[6],
            'zip': customer_info_dict[7],
            'sex': customer_info_dict[8],
            'phone': customer_info_dict[9],
        }
        edit_window = EntryWindow(self.database, self.left_frame, **cust)

