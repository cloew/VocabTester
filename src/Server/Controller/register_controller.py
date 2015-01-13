from Data.user import User
from Server.error import EMAIL_IN_USE
from Server.Controller.login_controller import LoginController

from kao_flask.ext.sqlalchemy.database import db

from kao_flask.controllers.json_controller import JSONController
from sqlalchemy.exc import IntegrityError

class RegisterController(JSONController):
    """ Controller to register a user """
    
    def performWithJSON(self):
        """ Create a User record with the given credentials """
        try:
            user = User(**self.json)
            db.session.add(user)
            db.session.commit()
            
            login = LoginController()
            login.json = self.json
            return login.performWithJSON()
        except IntegrityError:
            return EMAIL_IN_USE.toJSON()