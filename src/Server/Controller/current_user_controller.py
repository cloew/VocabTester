from auth_json_controller import AuthJSONController

from Data.user import User
from Server.error import NO_USER
from Server.Data.user_wrapper import UserWrapper

class CurrentUserController(AuthJSONController):
    """ Controller to return the currently signed in user """
    
    def performWithJSON(self, user=None):
        """ Convert the existing Word Lists to JSON """
        user = User.query.filter_by(id=user[u'id']).first()
        if user:
            return {'user':UserWrapper(user).toJSON()}
        return NO_USER.toJSON()