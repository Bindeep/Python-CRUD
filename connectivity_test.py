from Src.DbConnectionModule import DbConnection

connection_object = DbConnection('connection_test.db') # Instantiate Database Connection
cursor_object = connection_object.get_cursor_obj()  # get cursor object to perform execute function
print(cursor_object)
connection_object.commit() # commit changes to the database
connection_object.close_connection() # Destroy Database Connection