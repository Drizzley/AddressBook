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
        cursor.execute('SELECT address1 ' \
                       'FROM foodtown ' \
                       'WHERE ' \
                       'first_name = ' + '\"' + name_dict['first_name'] + '\" AND ' \
                       'last_name = ' + '\"' + name_dict['last_name'] + '\"')
        address = cursor.fetchone()
        print(address[0])

    def returnAllCustomerInfo(self, name_dict):
        cursor = self.db.cursor()
        cursor.execute('SELECT * ' \
                       'FROM foodtown ' \
                       'WHERE ' \
                       'first_name = \"' + name_dict['first_name'] + '\" AND ' \
                       'last_name = \"' + name_dict['last_name'] + '\"')
        address = cursor.fetchone()
        return address

    def deleteCustomerFromDB(self, name_dict):
        """Deletes the customer from the database"""
        cursor = self.db.cursor()
        cursor.execute('DELETE FROM foodtown ' \
                       'WHERE first_name = \"' + name_dict['first_name'] + '\" AND ' \
                       'last_name = \"' + name_dict['last_name'] + '\"')
        self.db.commit()

    def addCustomerToDB(self, customer_dict):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO foodtown(first_name, last_name, address1, address2, state,' \
                       ' city, zip, sex) ' \
                       'VALUES(\"' + customer_dict['first_name'] + '\",' + \
                       '\"' + customer_dict['last_name'] +'\", \"' + customer_dict['street'] + \
                       '\", \"' + customer_dict['apt'] + '\", \"' + customer_dict['state'] + '\", \"' + customer_dict['city'] + \
                       '\", \"' + customer_dict['zip'] + '\", \"' + customer_dict['sex'] + '\")')
        self.db.commit()
