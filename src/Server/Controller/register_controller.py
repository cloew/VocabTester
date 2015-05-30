from Data.user import User
from Server.error import EMAIL_IN_USE
from Server.Controller.create_controller import CreateController
from Server.Controller.login_controller import LoginController
from Server.helpers.record_value_provider import RecordValueProvider

from Server.decorators import requires_auth

from kao_flask.ext.sqlalchemy.database import db

from sqlalchemy.exc import IntegrityError



class RegisterController(CreateController):
    """ Controller to register a user """
    
    def __init__(self):
        """ Initialize the Register Controller """
        CreateController.__init__(self, User, recordValueProvider=RecordValueProvider({'nativeLanguage': lambda value: ('native_language_id', value['id'])}))
    
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