"""
Class that defines the windows that pops up when pressing 'Add'
on the main screen
"""
from tkinter import *

class EntryWindow(object):

    def __init__(self, database, left_frame, **customer_dict):
        """Constructor"""
        self.database = database
        self.left_frame = left_frame

        self.root = Toplevel()
        self.root.wm_title('Add New Person')
        self.top_frame = Frame(self.root)
        self.bottom_frame = Frame(self.root)

        # If passed customer, change button to 'edit' instead of 'add'
        if customer_dict:
            self.customer_data = {
                'first_name_id': customer_dict['first_name'], 
                'last_name_id': customer_dict['last_name']
            }
            self.done_button = Button(self.bottom_frame, text='Edit', command=self.editExistingCustomer)
        else:
            self.customer_data = None
            self.done_button = Button(self.bottom_frame, text='Add', command=self.createNewCustomer)

        self.done_button.pack(side=LEFT, padx=5, pady=5)
        self.cancel_button = Button(self.bottom_frame, text='Cancel', command=self.root.destroy)
        self.cancel_button.pack(side=LEFT)

        self.first_name = Label(self.top_frame, text='First Name:')
        self.last_name = Label(self.top_frame, text='Last Name:')
        self.phone_number = Label(self.top_frame, text='Phone:')
        self.street = Label(self.top_frame, text='Street:')
        self.apt_label = Label(self.top_frame, text='Apt:')
        self.city = Label(self.top_frame, text='City:')
        self.state = Label(self.top_frame, text='State:')
        self.zip = Label(self.top_frame, text='Zip:')

        self.first_name_box = Entry(self.top_frame)
        self.last_name_box = Entry(self.top_frame)
        self.phone_box = Entry(self.top_frame)
        self.street_box = Entry(self.top_frame)
        self.apt_box = Entry(self.top_frame)
        self.city_box = Entry(self.top_frame)
        self.state_box = Entry(self.top_frame, width=2)
        self.zip_box = Entry(self.top_frame, width=5)

        self.male_or_female = StringVar()
        self.male_or_female.set("m")
        self.male_button = Radiobutton(self.bottom_frame, text='Male', value="m", variable=self.male_or_female)
        self.female_button = Radiobutton(self.bottom_frame, text='Female', value="f", variable=self.male_or_female)

        self.pack_top_frame()

        self.top_frame.pack(side=TOP)
        self.bottom_frame.pack()

        if customer_dict:
            self.prefillTextboxes(customer_dict)

        self.root.mainloop()

    def pack_top_frame(self):
        """Packs all the labels and entries using grid"""
        self.first_name.grid(row=0, sticky=E)
        self.first_name_box.grid(row=0, column=1)

        self.last_name.grid(row=1, sticky=E)
        self.last_name_box.grid(row=1, column=1)

        self.phone_number.grid(row=2, sticky=E)
        self.phone_box.grid(row=2, column=1)

        self.street.grid(row=3, sticky=E)
        self.street_box.grid(row=3, column=1)

        self.apt_label.grid(row=4, sticky=E)
        self.apt_box.grid(row=4, column=1)

        self.city.grid(row=5, sticky=E)
        self.city_box.grid(row=5, column=1)

        self.state.grid(row=6, sticky=E)
        self.state_box.grid(row=6, column=1, sticky=W)

        self.zip.grid(row=7, sticky=E)
        self.zip_box.grid(row=7, column=1, sticky=W)
        
        self.male_button.pack()
        self.female_button.pack()
    
    def get_text(self):
        """Grab the text from the text boxes"""
        ATTRIBUTES = {
            'first_name': self.first_name_box.get(),
            'last_name': self.last_name_box.get(),
            'phone' : self.phone_box.get(),
            'street': self.street_box.get(),
            'apt': self.apt_box.get(),
            'city': self.city_box.get(),
            'state': self.state_box.get(),
            'zip': self.zip_box.get(),
            'sex': self.male_or_female.get()
        }

        if self.customer_data:
            ATTRIBUTES['first_name_id'] = self.customer_data['first_name_id']
            ATTRIBUTES['last_name_id'] = self.customer_data['last_name_id']

        return ATTRIBUTES

    def createNewCustomer(self):
        customer_dict = self.get_text()
        self.database.addCustomerToDB(customer_dict)
        self.left_frame.populateContactList()
        self.root.destroy()

    def editExistingCustomer(self):
        customer_dict = self.get_text()
        self.database.updateExistingCustomer(customer_dict)
        self.left_frame.populateContactList()
        self.root.destroy()

    def prefillTextboxes(self, customer_dict):
        self.first_name_box.insert(0, customer_dict['first_name'])
        self.last_name_box.insert(0, customer_dict['last_name'])
        self.phone_box.insert(0, customer_dict['phone'])
        self.street_box.insert(0, customer_dict['address1'])
        self.apt_box.insert(0, customer_dict['address2'])
        self.city_box.insert(0, customer_dict['city'])
        self.state_box.insert(0, customer_dict['state'])
        self.zip_box.insert(0, customer_dict['zip'])

