from cmd import Cmd
from Src.table_crud import CRUDTable
from Src.DbConnectionModule import DbConnection
from quick_sort import QuickSort
from search_algorithms import BinarySearch 

class MyPrompt(Cmd):

    intro = """ ***** Welcome to the UserCRUD Shell.. *****

   	Basic Command are: 
	connectdb
	createuser
	insert_data
        update data
        retrieve users
        delete users
        get all users
        drop table
	quit
    
	Type help <command> to show command details"""

    @staticmethod
    def print_func(self, user_data):
        if isinstance(user_data[0], tuple):
            for data in user_data:
                print(f""" ***** User Details of User {data[1]} *****
'id': {data[0]}\n'name': {data[1]}\n'email': {data[2]}\n'phone': {data[3]}
'Date of birth': {data[4]}\n'Gener': {data[5]}\n'Latitude': {data[6]}
'Longitude': {data[7]}\n'image': {data[8]}\n'Social Media': {data[9]}\n\n""")
        else:
            lst = ['id', 'name', 'email', 'phone', 'dob', 'gender', 'latitude',
            'longitude', 'image', 'social_media']
            for data in user_data:
                str_list = f" *** User details of {data['name']} *** \n"
                for item in lst:
                    str_list += f"{item}: {data[item]} \n"
                print(str_list)

    @staticmethod
    def populate_data():
        """Populate user table with user profile details."""
        values = dict()
        values['name'] = input('Enter Your full name : ')
        values['email'] = input('Enter Your email : ')
        values['phone'] = input('Enter Your phone number : ')
        values['gender'] = input(
            'Enter Your gender "Male" "Female" "Other" : ')
        values['dob'] = input('Enter Your Date of Birh : ')
        values['latitude'] = input('Enter Your latitude : ')
        values['longitude'] = input('Enter Your longitude : ')
        values['image'] = input('Enter Your image : ')
        values['social_media'] = input('Enter Your social_media : ')
        return values

    def do_connectdb(self, db_name):
        """Create database  ..name can be passed as argument like connectdb postgres."""
        if not db_name:
            db_name = input("Enter database that you want to connect :\n")
        else:
            pass
        self.connection_obj = CRUDTable(db_name)
        print("Connection Successful")

    def do_createuser(self, *args):
        """Create user table in database."""
        self.connection_obj.initialize_table()
        print("UserTable Created Successful")

    def do_get_all_users(self, *args):
        """get all data from userprofile takes no any extra arguments"""
        self.user_data = self.connection_obj.get_all()
        self.__class__.print_func(self, self.user_data)
    
    @staticmethod
    def do_all_users(self, *args):
        self.user_data = self.connection_obj.get_all()

    def do_retrieve_users(self, *args):
        """ Retrieve User profile key and value should be passed"""
        key = input("Provide key through which you want to retrieve user :\n")
        value = input(f"Provide {key} to retrieve :")
        self.user_data = self.connection_obj.retrieve_user(key, value)
        self.__class__.print_func(self, self.user_data)

    def do_insert_data(self, *args):
        """Populate user table with user profile details."""
        print("Provide data to insert")
        self.connection_obj.insert_into_table(**self.__class__.populate_data())
        print("Data Insertion Successful")

    def do_update_data(self, *args):
        """Update user profile details."""
        print("Provide data to update")
        self.connection_obj.update_into_table(**self.__class__.populate_data())
        print("Data Update Successful")

    def do_delete_users(self, value=None):
        """ Delete User profile, with desired key and value """
        if not value:
            key = input("Provide key through which you want to delete user :\n")
            value = input(f"Provide {key} to delete :")
        else:
            key = 'id'
            value = value
        self.connection_obj.delete_user(key, value)
        print("Deletion Successful")
  
    def do_drop_table(self, *args):
        """Drop user table."""
        self.connection_obj.drop_table()
        print("Table Dropped Successful")
      
    def do_sort_user(self, key=None):
        """sort user table with desired key"""
        if hasattr(self, 'user_data'):
            if key is None:
                key = input("Enter a field through which you want to sort :")
            else:
                key = key
            sort_obj  = QuickSort()
            result_set = sort_obj.resultset(self.user_data)
            sorted_data = sort_obj.sort(result_set, key=key)
            self.__class__.print_func(self, sorted_data)
            print(f"Sorted using {key}")
        else:
            self.do_all_users(self)
            self.do_sort_user(key=key)

    def do_search_user(self, item=None):
        """Search user profile."""
        if not item:
            key = input("Provide the key to search item :")
            item = input(f"Provide {key} of user to be searched :")
            try:
                item = int(item)
            except:
                item = item
        else:
            key = 'id'
            item = int(item)
        self.do_all_users(self)
        sort_obj  = QuickSort()
        result_set = sort_obj.resultset(self.user_data)
        sorted_data = sort_obj.sort(result_set, key=key)
        search_obj = BinarySearch()
        data = search_obj.search(sorted_data, item, key=key)
        print(data)

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit


if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = 'user@shell> '
    prompt.cmdloop()
