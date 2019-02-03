"""Class where all the database operations are done"""

import mysql.connector

class DataBaseClass(object):

    def __init__(self):
        self.cnx = mysql.connector.connect(
            user='root', 
            password='my-secret-pw',
            host='172.17.0.2',
            database='testdb'
        )

    def getNamesOfCustomers(self):
        """Returns a list with all the names"""
        people = []
        cursor = self.cnx.cursor()
        cursor.execute('SELECT first_name, last_name FROM foodtown ORDER BY last_name')
        results = cursor.fetchall()

        if results:
            for person in results:
                name = person[0] + ' ' + person[1]
                people.append(name)
        return people

    def returnAddressFromName(self, name_dict):
        cursor = self.cnx.cursor()
        get_customer_address = (
            'SELECT address1 FROM foodtown '
            'WHERE first_name = %(first_name)s AND last_name= %(last_name)s'
        )
        cursor.execute(get_customer_address, name_dict)
        address = cursor.fetchone()

    def returnAllCustomerInfo(self, name_dict):
        cursor = self.cnx.cursor()
        get_customer_info = (
            'SELECT * FROM foodtown '
            'WHERE first_name = %(first_name)s AND last_name = %(last_name)s'
        )
        cursor.execute(get_customer_info, name_dict)
        address = cursor.fetchone()
        return address

    def deleteCustomerFromDB(self, name_dict):
        """Deletes the customer from the database"""
        cursor = self.cnx.cursor()
        delete_from_operation = (
            'DELETE FROM foodtown '
            'WHERE first_name = %(first_name)s AND last_name = %(last_name)s'
        )
        cursor.execute(delete_from_operation, name_dict)
        self.cnx.commit()

    def updateExistingCustomer(self, customer_dict):
        """Updates existing customer info"""
        cursor = self.cnx.cursor()
        update_operation = (
            'UPDATE foodtown '
            'SET first_name = %(first_name)s, last_name = %(last_name)s, phone = %(phone)s, address1 = %(street)s, '
            'address2 = %(apt)s, state = %(state)s, city = %(city)s, zip = %(zip)s, sex = %(sex)s '
            'WHERE first_name = %(first_name_id)s AND last_name = %(last_name_id)s'
        )
        cursor.execute(update_operation, customer_dict)
        self.cnx.commit()

    def addCustomerToDB(self, customer_dict):
        cursor = self.cnx.cursor()
        insert_into_operation = (
            'INSERT INTO foodtown(first_name, last_name, address1, address2, state, city, zip, sex, phone)'
            'VALUES(%(first_name)s, %(last_name)s, %(city)s, %(apt)s, %(state)s, %(city)s, %(zip)s, %(sex)s, %(phone)s)'
        )
        cursor.execute(insert_into_operation, customer_dict)
        self.cnx.commit()
