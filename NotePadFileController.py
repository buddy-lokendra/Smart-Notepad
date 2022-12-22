# Import File Modul
import NotePadFileModel
import speech_recognition as s

# Create File_Controller Class
class File_Controller:
    # Dunder init
    def __init__(self):
        # Create Object of File_Model Class , which is inside NotePadFileModel
        self.file_model = NotePadFileModel.File_Model()

    # save the file
    def save_file(self,msg):
        self.file_model.save_file(msg)

    # save the file in secure way
    def save_as(self,msg):
        self.file_model.save_as(msg)

    # Read File content
    def read_file(self,url):
        self.msg,self.base = self.file_model.read_file(url)
        return (self.msg,self.base)

    # Create New File
    def new_file(self):
        self.file_model.new_file()

    # For Converting Speech to Text
    def take_query(self):
        print('take query')
        # Recongnizer is class in speech_recognition module
        sr = s.Recognizer()
        print('Say something:')
        # Microphone is function of speech_recognition module , Microphone represent device
        with s.Microphone() as m:
            audio = sr.listen(m)
            text = sr.recognize_google(audio, language='en-IN')
            return text