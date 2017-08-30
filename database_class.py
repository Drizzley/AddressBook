"""Class where all the database operations are done"""

import MySQLdb

class DataBaseClass(object):

    def __init__(self):
        self.db = MySQLdb.connect(
            host = 'localhost',
            user = 'testuser',
            passwd = 'testpassword',
            db = 'testdb'
        )

    def getNamesOfCustomers(self):
        """Returns a list with all the names"""
        people = []
        cursor = self.db.cursor()
        cursor.execute('SELECT first_name, last_name FROM foodtown ORDER BY last_name')
        results = cursor.fetchall()

        if results:
            for person in results:
                name = person[0] + ' ' + person[1]
                people.append(name)
        return people

    def returnAddressFromName(self, name_dict):
        cursor = self.db.cursor()
        get_customer_address = (
            'SELECT address1 FROM foodtown '
            'WHERE first_name = %(first_name)s AND last_name= %(last_name)s'
        )
        cursor.execute(get_customer_address, name_dict)
        address = cursor.fetchone()
        print(address[0])

    def returnAllCustomerInfo(self, name_dict):
        cursor = self.db.cursor()
        get_customer_info = (
            'SELECT * FROM foodtown '
            'WHERE first_name = %(first_name)s AND last_name = %(last_name)s'
        )
        cursor.execute(get_customer_info, name_dict)
        address = cursor.fetchone()
        return address

    def deleteCustomerFromDB(self, name_dict):
        """Deletes the customer from the database"""
        cursor = self.db.cursor()
        delete_from_operation = (
            'DELETE FROM foodtown '
            'WHERE first_name = %(first_name)s AND last_name = %(last_name)s'
        )
        cursor.execute(delete_from_operation, name_dict)
        self.db.commit()

    def addCustomerToDB(self, customer_dict):
        cursor = self.db.cursor()
        insert_into_operation = (
            'INSERT INTO foodtown(first_name, last_name, address1, address2, state, city, zip, sex, phone)'
            'VALUES(%(first_name)s, %(last_name)s, %(city)s, %(apt)s, %(state)s, %(city)s, %(zip)s, %(sex)s, %(phone)s)'
            )
        cursor.execute(insert_into_operation, customer_dict)
        self.db.commit()
