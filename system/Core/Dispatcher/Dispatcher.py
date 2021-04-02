import html.client

class Dispatcher:

    def __init__(self, URL_VAR, WEB_VAR, VIEW_MODEL_VAR, METHOD_VAR):
        #constructor to the dispatcher class
        self.WEB_VAR = html.client.HTTPSConnection("localhost", 80)
        self.WEB_VAR.request("GET", "/")


    def callback_motor(self):
        #callback motor method made to implement a callback function

    def url_maker(self):
        #this method implement url maker engine

    def get_route(self):
        #method to implement a route calling from its original class

    def dispatcher(self):
        #catalyzer for this class
