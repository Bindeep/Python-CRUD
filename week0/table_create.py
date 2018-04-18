from DbConnectionModule import DbConnection


class CreateTable:
    """
    Table Creation, Value insertion, Updating and Deletion of User Table
    """

    def __init__(self, db_name='test1.db'):

        self.connection_obj = DbConnection(db_name)
        self.cursor_obj = self.connection_obj.get_cursor_obj()

    def initialize_table(self): #  Initialize User Table

        create_statement = """CREATE TABLE User
        (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name char(30),
            Email text Not NUll UNIQUE,
            Phone varchar(15) NOT NULL UNIQUE,
            DOB char(10),
            Gender char(6) NOT NULL CHECK(Gender IN('Male', 'Female', 'Others')),
            Latitude varchar(100),
            Longitude varchar(100),
            Image varchar,
            Social_Media text
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
                    Name='{name}',\
                    DOB='{dob}', Gender='{gender}', Latitude='{latitude}',\
                    Longitude='{longitude}', Image='{image}', SocialMedia='{social_media}'\
                    WHERE Email='{email}'".format(**kwargs)
            self.cursor_obj.execute(update_statement)
            self.connection_obj.commit()
        except Exception as e:
            print(e)
    
    def retrieve_user(self, **kwargs):
        retrieve_statement = "SELECT * FROM User WHERE Email='{email}'".format(**kwargs)
        self.cursor_obj.execute(retrieve_statement)
        
    def delete_user(self, **kwargs):
        try:
            delete_statement = "DELETE FROM User WHERE Email='{email}'".format(**kwargs)
            self.cursor_obj.execute(delete_statement)
        except Exception as e:
            print(e)
    
    def drop_table(self): #  Delete User Table
        drop_statement = "DROP TABLE IF EXISTS User"
        self.cursor_obj.execute(drop_statement)

  
# a = CreateTable('test1.db')
# a.initialize_table()
# a.insert_into_table(name='lakal', email='bindeep', phone='kalka', gender='Male', dob='afaf', latitude='1234', longitude='09876', image='kakakka', social_media='uauau')
# a.update_into_table(name='lfakal', email='bindeep', phone='kffalka', gender='Male', dob='affaf', latitude='1234', longitude='09876', image='kakakka', social_media='uafuau')
# a.delete_user(email='bindeep')
# a.drop_table()