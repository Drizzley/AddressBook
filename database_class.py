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
