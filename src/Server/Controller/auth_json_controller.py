from Server.decorators import requires_auth
from kao_flask.controllers.json_controller import JSONController

class AuthJSONController(JSONController):
    """ Controller Base that requires the user to be authorized before running """
    
    def __init__(self):
        """ Initialize the JSON Controller with its required decorators """
        JSONController.__init__(self, decorators=[requires_auth])