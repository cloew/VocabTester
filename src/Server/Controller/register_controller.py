from Data.user import User
from Server.error import EMAIL_IN_USE
from Server.Controller.login_controller import LoginController

from Server.decorators import requires_auth

from kao_flask.ext.sqlalchemy import db, CreateController, RecordValueProvider

from sqlalchemy.exc import IntegrityError

class RegisterController(CreateController):
    """ Controller to register a user """
    
    def __init__(self):
        """ Initialize the Register Controller """
        CreateController.__init__(self, User, None, recordValueProvider=RecordValueProvider({'nativeLanguage': lambda value: ('native_language_id', value['id'])}))
    
    def performWithJSON(self, json=None):
        """ Create a User record with the given credentials """
        try:
            print(json)
            json['is_admin'] = False
            user = self.create(json)

            login = LoginController()
            return login.performWithJSON(json=json)
        except IntegrityError:
            return EMAIL_IN_USE.toJSON()