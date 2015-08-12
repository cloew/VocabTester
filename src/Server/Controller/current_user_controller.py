from .auth_json_controller import AuthJSONController

from Data.user import User
from Server.error import NO_USER
from Server.helpers.json_factory import toJson

class CurrentUserController(AuthJSONController):
    """ Controller to return the currently signed in user """
    
    def performWithJSON(self, json=None, user=None):
        """ Convert the existing Word Lists to JSON """
        if user:
            return {'user':toJson(user)}
        return NO_USER.toJSON()