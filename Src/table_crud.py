try:
    from DbConnectionModule import DbConnection
except:
    from .DbConnectionModule import DbConnection

class CRUDTable:
    """
    Table Creation, Value insertion, Updating and Deletion of User Table
    """

    def __init__(self, database):

        self.connection_obj = DbConnection(database)
        self.cursor_obj = self.connection_obj.get_cursor_obj()

    def get_cursor(self):
        self.cursor_obj =  self.connection_obj.get_cursor_obj()
        return self.cursor_obj

    def initialize_table(self): #  Initialize User Table

        #for auto increment in sqlite (ID INTEGER PRIMARY KEY AUTOINCREMENT) in postgres(id serial primary key)
        # int is supported by postgres unlike sqlite that supports integer

        create_statement = """
        CREATE TABLE IF NOT EXISTS userprofile
        (
            id serial unique,
            name varchar(100),
            email varchar(100) Not NUll,
            phone varchar(50) NOT NULL,
            dob varchar(20),
            gender varchar(8),
            latitude varchar(100),
            longitude varchar(100),
            image varchar,
            social_media varchar(100)
        )"""
        self.cursor_obj.execute(create_statement)
        self.connection_obj.commit()
    
    def get_all(self): #  List all users from UserTable
            fetch_statement = "SELECT * from userprofile limit 10"
            # return self.cursor_obj.execute(fetch_statement).fetchall() #in pg should fetch using 
            # cursor_obj
            self.cursor_obj.execute(fetch_statement)
            return self.cursor_obj.fetchall()

    def insert_into_table(self, **kwargs): #  Insert User details
        insert_statement = "INSERT INTO userprofile"
        fields = list()
        values = list()
        for k, v in kwargs.items():
            fields.append(k)
            values.append(v)
        user_fields = tuple(fields)
        user_values = tuple(values)
        # insert_statement += f"{user_fields} " + "VALUES " + f"{user_values}"
        #  postgres doesnot support insert into('id', 'name')values.. it only supports insert into(id, name)
        # so we remove quote
        insert_statement += f"{user_fields}"
        insert_statement = insert_statement.replace("'","")
        insert_statement += "VALUES" + f"{user_values}"
        self.cursor_obj.execute(insert_statement)
        self.connection_obj.commit()

    def update_into_table(self, **kwargs): #  Update User details
        try:
            update_statement = " UPDATE userprofile SET\
                    Name='{name}',\
                    DOB='{dob}', Gender='{gender}', Latitude='{latitude}',\
                    Longitude='{longitude}', Image='{image}', social_media='{social_media}'\
                    WHERE Email='{email}'".format(**kwargs)
            self.cursor_obj.execute(update_statement)
            self.connection_obj.commit()
        except Exception as e:
            print(e)
    
    def retrieve_user(self, key, value):
        retrieve_statement = f"SELECT * FROM userprofile WHERE {key} ='{value}'"
        self.cursor_obj.execute(retrieve_statement)
        return self.cursor_obj.fetchall()
        
    def delete_user(self, key, value):
        try:
            delete_statement = f"DELETE FROM userprofile WHERE {key}='{value}'"
            self.cursor_obj.execute(delete_statement)
        except Exception as e:
            print(e)
    
    def drop_table(self): #  Delete User Table
        drop_statement = "DROP TABLE IF EXISTS userprofile"
        self.cursor_obj.execute(drop_statement)
