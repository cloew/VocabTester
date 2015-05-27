from Data.user import User
from Server.helpers.json_factory import toJson
from Server.helpers.record_value_provider import RecordValueProvider
from Server.helpers.token_builder import BuildToken
from Server.Controller.update_controller import UpdateController

class UpdateUserController(UpdateController):
    """ Controller to update a User """
    
    def __init__(self):
        """ Initialize the Update User Controller """
        UpdateController.__init__(self, User, recordValueProvider=RecordValueProvider({'nativeLanguage': lambda value: ('native_language_id', value['id'])}))
    
    def performWithJSON(self, **kwargs):
        """ Remove the record """
        user = kwargs['user']
        updatedUser = UpdateController.update(self, user.id, kwargs['json'])
        return {"token": BuildToken(updatedUser), "user": toJson(updatedUser)}