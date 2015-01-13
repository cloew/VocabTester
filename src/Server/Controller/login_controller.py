from Data.user import User
from Server.Data.token_builder import BuildToken

from kao_flask.ext.sqlalchemy.database import db

from kao_flask.controllers.json_controller import JSONController

class LoginController(JSONController):
    """ Controller to login a user """
    
    def performWithJSON(self):
        """ Create a User record with the given credentials """
        user = User.query.filter_by(email=self.json['email']).first()
        if user and user.checkPassword(self.json['password']):
            print "Logged In"
            return {'token':BuildToken(user)}, 201
        else:
            print "Failed to login"
            return {'code':1, 'message':'Invalid Credentials'}, 401