from Data.user import User
from Server.error import INVALID_CREDS
from Server.Data.token_builder import BuildToken
from Server.Data.json_factory import toJson

from kao_flask.ext.sqlalchemy.database import db

from kao_flask.controllers.json_controller import JSONController

class LoginController(JSONController):
    """ Controller to login a user """
    
    def performWithJSON(self, json=None):
        """ Create a User record with the given credentials """
        user = User.query.filter_by(email=json['email']).first()
        if user and user.checkPassword(json['password']):
            return {'token':BuildToken(user), 'user':toJson(user)}, 201
        else:
            return INVALID_CREDS.toJSON()