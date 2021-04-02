import os.path

class ViewModel:
    """docstring fo ViewModel."""

    def __init__(self, MIDDLEWARE, INTERFACE):
        self.MIDDLEWARE
        self.INTERFACE

    def view_method(self):
        # method that require the view and use it in the programme
        if os.path.isfile('filename.txt'):
            print ("File exist")
        else:
            print ("File not exist")

    def model_method(self):
        # links the model class to the viewmodel concerned
        if os.path.isfile('filename.txt'):
            print ("File exist")
        else:
            print ("File not exist")

    def json_parser(self):
        # Json version of the model data in the class

    def relayable(self):
        # Additionale adjustment in the class
