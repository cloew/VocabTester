from Data.token_builder import BuildToken
from Data.user import User

from kao_flask.ext.sqlalchemy.database import db

from kao_flask.controllers.json_controller import JSONController

class LoginController(JSONController):
    """ Controller to login a user """
    
    def performWithJSON(self):
        """ Create a User record with the given credentials """
        user = User.query.filter_by(email=self.json['email']).first()
        if user.checkPassword(self.json['password']):
            print "Logged In"
        else:
            print "Failed to login"
        return {'token':BuildToken(user)} # Should return the token and User object