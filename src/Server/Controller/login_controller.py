from Data.user import User
from Server.error import INVALID_CREDS
from Server.Data.token_builder import BuildToken
from Server.Data.user_wrapper import UserWrapper

from kao_flask.ext.sqlalchemy.database import db

from kao_flask.controllers.json_controller import JSONController

class LoginController(JSONController):
    """ Controller to login a user """
    
    def performWithJSON(self, json=None):
        """ Create a User record with the given credentials """
        user = User.query.filter_by(email=json['email']).first()
        if user and user.checkPassword(json['password']):
            return {'token':BuildToken(user), 'user':UserWrapper(user).toJSON()}, 201
        else:
            return INVALID_CREDS.toJSON()