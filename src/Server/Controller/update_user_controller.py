from Data.user import User
from Server.helpers.json_factory import toJson
from Server.helpers.token_builder import BuildToken

from Server.decorators import requires_auth
from kao_flask.ext.sqlalchemy import UpdateController, RecordValueProvider

class UpdateUserController(UpdateController):
    """ Controller to update a User """
    
    def __init__(self):
        """ Initialize the Update User Controller """
        UpdateController.__init__(self, User, toJson, decorators=[requires_auth], 
    							  recordValueProvider=RecordValueProvider({'nativeLanguage': lambda value: ('native_language_id', value['id'])}))
    
    def performWithJSON(self, **kwargs):
        """ Remove the record """
        user = kwargs['user']
        updatedUser = UpdateController.update(self, user.id, kwargs['json'])
        return {"token": BuildToken(updatedUser), "user": toJson(updatedUser)}