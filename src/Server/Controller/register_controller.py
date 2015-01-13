from Data.user import User
from Server.Controller.login_controller import LoginController

from kao_flask.ext.sqlalchemy.database import db

from kao_flask.controllers.json_controller import JSONController

class RegisterController(JSONController):
    """ Controller to register a user """
    
    def performWithJSON(self):
        """ Create a User record with the given credentials """
        user = User(**self.json)
        db.session.add(user)
        db.session.commit()
        
        login = LoginController()
        login.json = self.json
        return login.performWithJSON()