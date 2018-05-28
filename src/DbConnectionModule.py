import sqlite3
from sqlite3 import Error
import logging
import psycopg2
import os

hostname = '127.0.0.1'
username = os.environ.get('postgresuser')
password = os.environ.get('postgrespw')
database_name = os.environ.get('postgresdb')

class DbConnection:

    """
     Create a database connection to a database.
    """

    def __init__(self, database):

        try:
            if database == "sqlite3":
                self.connection_obj = sqlite3.connect(f'../Database/sqlite3')
            else:
                self.connection_obj = psycopg2.connect(host=hostname, user=username, password=password, dbname=database_name)

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
