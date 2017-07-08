"""
Class that defines the windows that pops up when pressing 'Add'
on the main screen
"""
from tkinter import *

class EntryWindow(object):

    def __init__(self):
        """Constructor"""
        self.root = Tk()
        self.top_frame = Frame(self.root)
        self.bottom_frame = Frame(self.root)

        self.done_button = Button(self.bottom_frame, text='Done', command=self.print_all_text)
        self.done_button.pack(side=LEFT, padx=5, pady=5)
        self.cancel_button = Button(self.bottom_frame, text='Cancel', command=self.root.destroy)
        self.cancel_button.pack(side=LEFT)

        self.first_name = Label(self.top_frame, text='First Name:')
        self.last_name = Label(self.top_frame, text='Last Name:')
        self.street = Label(self.top_frame, text='Street:')
        self.city = Label(self.top_frame, text='City:')
        self.state = Label(self.top_frame, text='State:')
        self.zip = Label(self.top_frame, text='Zip:')

        self.first_name_box = Entry(self.top_frame)
        self.last_name_box = Entry(self.top_frame)
        self.street_box = Entry(self.top_frame)
        self.city_box = Entry(self.top_frame)
        self.state_box = Entry(self.top_frame)
        self.zip_box = Entry(self.top_frame)

        self.pack_top_frame()

        self.top_frame.pack(side=TOP)
        self.bottom_frame.pack()

        self.root.mainloop()

    def pack_top_frame(self):
        """Packs all the labels and entries using grid"""
        self.first_name.grid(row=0)
        self.first_name_box.grid(row=0, column=1)

        self.last_name.grid(row=1)
        self.last_name_box.grid(row=1, column=1)

        self.street.grid(row=2)
        self.street_box.grid(row=2, column=1)

        self.city.grid(row=3)
        self.city_box.grid(row=3, column=1)

        self.state.grid(row=4)
        self.state_box.grid(row=4, column=1)

        self.zip.grid(row=5)
        self.zip_box.grid(row=5, column=1)
    
    def get_text(self):
        """Grab the text from the text boxes"""
        ATTRIBUTES = {
            'first_name': self.first_name_box.get(),
            'last_name': self.last_name_box.get(),
            'street': self.street_box.get(),
            'city': self.city_box.get(),
            'state': self.state_box.get(),
            'zip': self.zip_box.get()
        }
        return ATTRIBUTES
    
    def print_attributes(self, attributes):
        """Print info from text boxes"""
        print(attributes['first_name'] + ' ' + attributes['last_name'])
        print(attributes['street'])
        print(attributes['city'] + ', ' + attributes['state'] + ', ' + attributes['zip'])

    def print_all_text(self):
        ATTRIBUTES = self.get_text()
        self.print_attributes(ATTRIBUTES)
        self.root.destroy()
    