from cmd import Cmd
from Src.table_crud import CRUDTable
from Src.DbConnectionModule import DbConnection


class MyPrompt(Cmd):

    intro = """Welcome to the UserCRUD Shell..
   	Basic Command are 
	connectdb
	createuser
	insert_data
	quit
	Type help <command> to show command details"""

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit

    def do_connectdb(self, db_name):
        """Create database name ..name can be passed as argument CRUDTable('db_name')."""
        self.connection_obj = CRUDTable(db_name)
        print("Connection Successful")

    def do_createuser(self, *args):
        """Create user table in database."""
        self.connection_obj.initialize_table()
        print("User Created Successful")

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

    def do_insert_data(self, *args):
        """Populate user table with user profile details."""
        self.connection_obj.insert_into_table(**self.__class__.populate_data())
        print("Data Insertion Successful")

    def do_update_data(self, *args):
        """Update user profile details."""
        self.connection_obj.update_into_table(**self.__class__.populate_data())
        print("Data Update Successful")

    def do_drop_table(self, *args):
        """Populate user table with user profile details."""
        self.connection_obj.drop_table()
        print("Table Dropped Successful")

if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = 'user@shell> '
    prompt.cmdloop()
