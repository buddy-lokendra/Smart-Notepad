# import necessary Modeles
import os.path
import string
import traceback
from tkinter import filedialog

# Create File Model Class
class File_Model:

    # Dunder init method
    def __init__(self):
        # url contain path of file, which user select by filedialog.askopenfilename
        self.url = ''
        # this key hold a-z + A-Z + 0-9 , for Encoding and Decoding Purpose
        self.key = string.ascii_letters +''.join([str(x) for x in range(0,10)])
        # offset is logic of encoding and decoding
        self.offset = 5

    # used to Encrypt file data , it is called by
    def encrypt(self, plaintext):
        result = ''
        for l in plaintext:
            try:
                i = (self.key.index(l) + self.offset) % 62
                result += self.key[i]
            except ValueError:
                result += l
        return result

    # Used to Decrypt file data , it is used by
    def decrypt(self,ciphertext):
        result = ''
        for ch in ciphertext:
            try:
                ind = self.key.index(ch)
                ind = (ind - self.offset) % 62
                result += self.key[ind]
            except ValueError:
                result += ch
        return result

    # Used to get file path by user , it use filedialog.askopenfilename
    def open_file(self):
        self.url = filedialog.askopenfilename(title='Select File',filetypes=[("Text Documents", "*.*")])

    # Used to delete path for url instance variable
    def new_file(self):
        self.url = ''

    # Used to save as secured file
    def save_as(self, msg):
        content = msg
        encrypted = self.encrypt(content)
        self.url = filedialog.asksaveasfile(mode='w', defaultextension='.ntxt',filetypes=([("All Files", "*.*"), ("Text Documents", "*.txt")]))
        self.url.write(encrypted)
        filepath = self.url.name
        self.url.close()
        self.url = filepath

    # Used to Save file
    def save_file(self, msg):
        if self.url == "":
            self.url = filedialog.asksaveasfilename(title='Select File', defaultextension='.ntxt',filetypes=[("Text Documents", "*.*")])
        filename, file_extension = os.path.splitext(self.url)
        content = msg
        if file_extension in '.ntxt':
            content = self.encrypt(content)
        with open(self.url, 'w', encoding='utf-8') as fw:
            fw.write(content)

    #  Read file content
    def read_file(self,url=''):
            if url != '':
                self.url =url
            else:
                self.open_file()
            base = os.path.basename(self.url)
            file_name,file_extension = os.path.splitext(self.url)

            fr = open(self.url,'r')
            contents = fr.read()
            if file_extension == '.ntxt':
                contents = self.decrypt(contents)
            fr.close()
            return contents,base




# testing
# normal = 'BHOPAL'
# obj = File_Model()
# cipher = obj.encrypt(normal)
# nor = obj.decrypt(cipher)
# print(cipher)
# print(nor)