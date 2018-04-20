import json
import sqlite3

class ExecuteMany:

    def __init__(self, db_path):
        self.connection_obj = sqlite3.connect(db_path)
    
    def load_data(self, file_path):
        return json.load(open(file_path))

    def get_cursor_obj(self):
        return self.connection_obj.cursor()
    
    def insert_many(self, file_path):
        self.get_cursor_obj().executemany(
            '''INSERT INTO User (name, email, phone, gender, latitude, longitude, image, social_media)
            VALUES(
                :name, :email, :phone, :gender,
                :latitude, :longitude, :image,
                :social_media
            )''',self.load_data(file_path))
        self.connection_obj.commit()


conn_0bj = ExecuteMany('../secondb') # connect to existing database to populate User table
conn_0bj.insert_many('MOCK_DATA.json')  # insert data by providing data file path 
