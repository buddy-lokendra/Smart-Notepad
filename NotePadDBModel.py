# import necessary modules
from cx_Oracle import *
from traceback import *


# create Class of DB_Module
class Db_Model:

    # Dunder init method
    def __init__(self):
        # file_dict --> key = file_name , value = (file_path,file_owner,file_pwd)
        self.file_dict = {}
        # check wheather Oracle Database Connected or Not
        self.db_status = True
        self.conn = None
        self.cur = None

        # try to connect with Oracle database
        try:
            # username / password @ 127.0.0.1 / xe
            self.conn = connect("mojo/mojo@127.0.0.1/xe")
            print("Connect Successfully ")
            self.cur = self.conn.cursor()
        except DatabaseError:
            self.db_status = False
            print("DB Error ", format_exc())

    # Check Connected to Database or Not
    def get_db_status(self):
        return self.db_status

    # Close DataBase Connection
    def close_db_connection(self):
        if self.cur is not None:
            self.cur.close()
            print("Cursor closed")
        if self.conn is not None:
            self.conn.close()
            print("Connection closed")

    # Add File Details in file_dict instance variable
    def add_file(self, file_name, file_path, file_owner, file_pwd):
        self.file_dict[file_name] = (file_path, file_owner, file_pwd)
        print("file added:", self.file_dict[file_name])

    # Try to Fetch file_path from file_dict instance variable
    def get_file_path(self, file_name):
        return self.file_dict[file_name][0]

    # try to add file_details in Oracle DataBase
    def add_file_to_db(self, file_name, file_path, file_owner, file_pwd):
        self.cur.execute('select max(file_id) from mysecurefiles')
        last_file_id = self.cur.fetchone()[0]
        next_file_id = 1
        if last_file_id is not None:
            next_file_id = last_file_id[0] + 1
        self.cur.execute('insert into mysecurefiles values (:1, :2, :3, :4, :5)',
                         (next_file_id, file_name, file_path, file_owner, file_pwd), )
        self.conn.commit()
        return 'file successfully added to the database'

    # Load Files Details form DataBase and insert it into file_dict instance variable
    def load_files_from_db(self):
        self.cur.execute('select file_name,file_path,file_owner,file_pwd from mysecurefiles')
        record_added = False
        for file_name, file_path, file_owner, file_pwd in self.cur:
            self.file_dict[file_name] = (file_path, file_owner, file_pwd)
            record_added = True
        if record_added == True:
            return 'File Populated'
        else:
            return 'No Files Present in you DB'

    # Remove file Details form DataBase as well as from file_dict instance variable
    def remove_file_from_db(self, file_name):
        self.cur.execute('delete from mysecurefiles where file_name =  :1', (file_name,))
        if self.cur.rowcount == 0:
            return 'File not present in the DB'
        else:
            self.file_dict.pop(file_name)
            self.conn.commit()
            return 'file delete from db'

    # Check file is Secured File or Not , by fetching data from file_dict instance variable
    def is_secure_file(self, file_name):
        return file_name in self.file_dict

    # Get File password form file_dict instance variable by passing file_name
    def get_file_pwd(self, file_name):
        file_path, file_owner, file_pwd = self.file_dict[file_name]
        return file_pwd

    # Return Number of File Present in file_dict (Oracle DataBase , Secured File)
    def get_file_count(self):
        return len(self.file_dict)

    # Get File Owner from file_dict instance Variable by passing file_name
    def get_file_owner(self, file_name):
        file_path, file_owner, file_pwd = self.file_dict[file_name]
        return file_owner

# testing
# obj = Db_Model()
