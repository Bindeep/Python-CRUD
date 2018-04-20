import sqlite3
from sqlite3 import Error
import logging


class DbConnection:

    """
     Create a database connection to a database.
    """

    def __init__(self, db_name='user.db'):

        try:
            self.connection_obj = sqlite3.connect(db_name)

        except Error:
            logging.error(f'Connection Unsuccessful with {Error}')

    def get_cursor_obj(self):
        self.cursor_obj = self.connection_obj.cursor()
        return self.cursor_obj

    def commit(self):
        self.connection_obj.commit()

    def close_connection(self):
        if self.connection_obj:
            self.connection_obj.close()

a = DbConnection('a.db')
a.get_cursor_obj()
