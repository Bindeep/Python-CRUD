try:
    from DbConnectionModule import DbConnection
except:
    from Src.DbConnectionModule import DbConnection

class CRUDTable:
    """
    Table Creation, Value insertion, Updating and Deletion of User Table
    """

    def __init__(self, db_name):

        self.connection_obj = DbConnection(db_name)
        self.cursor_obj = self.connection_obj.get_cursor_obj()

    def initialize_table(self): #  Initialize User Table

        create_statement = """CREATE TABLE User
        (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name char(30),
            email text Not NUll UNIQUE,
            phone varchar(15) NOT NULL,
            dob char(10),
            gender char(6) NOT NULL CHECK(Gender IN('Male', 'Female', 'Others')),
            latitude varchar(100),
            longitude varchar(100),
            image varchar,
            social_media text
        )"""
        self.cursor_obj.execute(create_statement)
    
    def get_all(self): #  List all users from UserTable
            fetch_statement = "SELECT * from User"
            return self.cursor_obj.execute(fetch_statement).fetchall()

    def insert_into_table(self, **kwargs): #  Insert User details
        insert_statement = "INSERT INTO User "
        fields = list()
        values = list()
        for k, v in kwargs.items():
            fields.append(k)
            values.append(v)
        user_fields = tuple(fields)
        user_values = tuple(values)
        insert_statement += f"{user_fields} " + "VALUES " + f"{user_values}"
        self.cursor_obj.execute(insert_statement)
        self.connection_obj.commit()

    def update_into_table(self, **kwargs): #  Update User details
        try:
            update_statement = " UPDATE User SET\
                    name='{name}',\
                    dob='{dob}', gender='{gender}', latitude='{latitude}',\
                    longitude='{longitude}', image='{image}', social_media='{social_media}'\
                    WHERE email='{email}'".format(**kwargs)
            self.cursor_obj.execute(update_statement)
            self.connection_obj.commit()
        except Exception as e:
            print(e)
    
    def retrieve_user(self, **kwargs):
        retrieve_statement = "SELECT * FROM User WHERE email='{email}'".format(**kwargs)
        self.cursor_obj.execute(retrieve_statement)
        
    def delete_user(self, **kwargs):
        try:
            delete_statement = "DELETE FROM User WHERE email='{email}'".format(**kwargs)
            self.cursor_obj.execute(delete_statement)
        except Exception as e:
            print(e)
    
    def drop_table(self): #  Delete User Table
        drop_statement = "DROP TABLE IF EXISTS User"
        self.cursor_obj.execute(drop_statement)


# from heap_sort import heapify
# a = CRUDTable() # initialization testing and populate 200 rows with another script 
# a.initialize_table()
# a.insert_into_table(name='lakal', email='bindeep', phone='kalka', gender='Male', dob='afaf', latitude='1234', longitude='09876', image='kakakka', social_media='uauau')
# a.update_into_table(name='lfakal', email='bindeep', phone='kffalka', gender='Male', dob='affaf', latitude='1234', longitude='09876', image='kakakka', social_media='uafuau')
# a.delete_user(email='bindeep')
# a.drop_table()

# a = CRUDTable()
# b = a.cursor_obj.execute("SELECT * FROM TestSort").fetchall()

# def sorting(key):
#     name_list = list()
#     for i in b:
#         name_list.append(i[0])
