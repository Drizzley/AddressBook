"""
Class that defines the windows that pops up when pressing 'Add'
on the main screen
"""
from tkinter import *

class EntryWindow(object):

    def __init__(self, database, left_frame):
        """Constructor"""
        self.database = database
        self.left_frame = left_frame

        self.root = Tk()
        self.root.wm_title('Add New Person')
        self.top_frame = Frame(self.root)
        self.bottom_frame = Frame(self.root)

        self.done_button = Button(self.bottom_frame, text='Done', command=self.createNewCustomer)
        self.done_button.pack(side=LEFT, padx=5, pady=5)
        self.cancel_button = Button(self.bottom_frame, text='Cancel', command=self.root.destroy)
        self.cancel_button.pack(side=LEFT)

        self.first_name = Label(self.top_frame, text='First Name:')
        self.last_name = Label(self.top_frame, text='Last Name:')
        self.street = Label(self.top_frame, text='Street:')
        self.apt_label = Label(self.top_frame, text='Apt:')
        self.city = Label(self.top_frame, text='City:')
        self.state = Label(self.top_frame, text='State:')
        self.zip = Label(self.top_frame, text='Zip:')

        self.first_name_box = Entry(self.top_frame)
        self.last_name_box = Entry(self.top_frame)
        self.street_box = Entry(self.top_frame)
        self.apt_box = Entry(self.top_frame)
        self.city_box = Entry(self.top_frame)
        self.state_box = Entry(self.top_frame, width=2)
        self.zip_box = Entry(self.top_frame, width=5)

        self.pack_top_frame()

        self.male_or_female = ''
        Radiobutton(self.bottom_frame, text='Male', variable=self.male_or_female, value='m').pack(anchor=W)
        Radiobutton(self.bottom_frame, text='Female', variable=self.male_or_female, value='f').pack(anchor=W)

        self.top_frame.pack(side=TOP)
        self.bottom_frame.pack()

        self.root.mainloop()

    def pack_top_frame(self):
        """Packs all the labels and entries using grid"""
        self.first_name.grid(row=0, sticky=E)
        self.first_name_box.grid(row=0, column=1)

        self.last_name.grid(row=1, sticky=E)
        self.last_name_box.grid(row=1, column=1)

        self.street.grid(row=2, sticky=E)
        self.street_box.grid(row=2, column=1)

        self.apt_label.grid(row=3, sticky=E)
        self.apt_box.grid(row=3, column=1)

        self.city.grid(row=4, sticky=E)
        self.city_box.grid(row=4, column=1)

        self.state.grid(row=5, sticky=E)
        self.state_box.grid(row=5, column=1, sticky=W)

        self.zip.grid(row=6, sticky=E)
        self.zip_box.grid(row=6, column=1, sticky=W)
    
    def get_text(self):
        """Grab the text from the text boxes"""
        ATTRIBUTES = {
            'first_name': self.first_name_box.get(),
            'last_name': self.last_name_box.get(),
            'street': self.street_box.get(),
            'apt': self.apt_box.get(),
            'city': self.city_box.get(),
            'state': self.state_box.get(),
            'zip': self.zip_box.get(),
            'sex': self.male_or_female
        }
        return ATTRIBUTES

    def createNewCustomer(self):
        customer_dict = self.get_text()
        self.database.addCustomerToDB(customer_dict)
        self.left_frame.populateContactList()
        self.root.destroy()
