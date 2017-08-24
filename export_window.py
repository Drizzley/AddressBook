"""Class that holds the window for the export button"""

from tkinter import *
import csv

class ExportWindow(object):

    def __init__(self, customer_dict):
        """Constructor"""
        self.customer_dict = customer_dict
        self.root = Toplevel()
        self.root.wm_title('Export Customer')
        self.root.geometry('300x170')
        self.top_frame = Frame(self.root)
        self.bottom_frame = Frame(self.root)
        self.button_frame = Frame(self.root)

        self.name_label = Label(self.top_frame, text=customer_dict['full_name'])
        self.address_1_label = Label(self.top_frame, text=customer_dict['address_1'])
        if customer_dict['address_2'] != '':
            self.address_2_label = Label(self.top_frame, text=customer_dict['address_2'])
        self.address_3_label = Label(self.top_frame, text=customer_dict['address_3'])


        self.name_label.pack()
        self.address_1_label.pack()
        if customer_dict['address_2'] != '':
            self.address_2_label.pack()
        self.address_3_label.pack()

        self.top_frame.pack(side=TOP)

        self.cash_or_credit = StringVar()
        self.cash_or_credit.set('cash')
        Radiobutton(self.bottom_frame, text='Cash', variable=self.cash_or_credit, value='cash').pack(anchor=W)
        Radiobutton(self.bottom_frame, text='Credit', variable=self.cash_or_credit, value='credit').pack(anchor=W)

        self.total_label = Label(self.bottom_frame, text='Total $:')
        self.total_entry_box = Entry(self.bottom_frame,width=7)
        self.total_label.pack(side=LEFT)
        self.total_entry_box.pack(side=LEFT)

        self.export_button = Button(self.button_frame, text='Export', command=self.exportToCSV)
        self.export_button.pack(side=BOTTOM)

        self.bottom_frame.pack()
        self.button_frame.pack()
        self.root.mainloop()

    def exportToCSV(self):
        payment_method = self.cash_or_credit.get() + ': $' + self.total_entry_box.get()
        with open('customer.csv', 'w') as csvfile:
            write_file = csv.writer(csvfile)
            write_file.writerow([self.customer_dict['full_name']])
            write_file.writerow([self.customer_dict['address_1']])
            if self.customer_dict['address_2'] != '':
                write_file.writerow([self.customer_dict['address_2']])
            write_file.writerow([self.customer_dict['address_3']])
            write_file.writerow([payment_method])
        self.root.destroy()

