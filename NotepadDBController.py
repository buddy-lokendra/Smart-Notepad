# import DB Model File
import NotePadDBModel

# Create Class Db_controller
class Db_controller:
    # Dunder init
    def __init__(self):
        # Here we create Object of Db_Model Class as instance variable , which is present in NotePadDBModel
        self.db_model = NotePadDBModel.Db_Model()

    # Check Weather DataBase is Connected or Not
    def get_db_status(self):
        return self.db_model.get_db_status()

    # Disconnect our DataBase if it is Connected
    def close_notepad(self):
        self.db_model.close_db_connection()

    # Get File Path
    def get_file_path(self,file_name):
        return self.db_model.get_file_path(file_name)

    # Get File Password
    def get_file_pwd(self,file_name):
        return self.db_model.get_file_pwd(file_name)

    # Check Weather File is Secured or Not
    def if_secure_file(self,file_name):
        return self.db_model.is_secure_file(file_name)

    # Add File Detail to DataBase
    def add_file(self,file_name,file_path,file_owner,file_pwd):
        if file_path == '':
            return ""
        if file_name in self.db_model.file_dict:
            return 'File Already Present'
        self.db_model.add_file(file_name,file_path,file_owner,file_pwd)
        self.db_model.add_file_to_db(file_name,file_path,file_owner,file_pwd)
        return 'File Added Successfully'

    # Remove File Details form DataBase
    def remove_file(self,file_name):
        result = self.db_model.remove_file_from_db(file_name)
        return result

    # Load All File Details From DataBase
    def load_files_from_db(self):
        self.db_model.load_files_from_db()
        return  self.db_model.file_dict

    # Count Secured File
    def get_file_count(self):
        return self.db_model.get_file_count()
