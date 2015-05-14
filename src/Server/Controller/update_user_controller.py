from Data.user import User
from Server.helpers.json_factory import toJson
from Server.helpers.token_builder import BuildToken
from Server.Controller.update_controller import UpdateController

class UpdateUserController(UpdateController):
    """ Controller to update a User """
    
    def __init__(self):
        """ Initialize the Update User Controller """
        UpdateController.__init__(self, User)
    
    def performWithJSON(self, **kwargs):
        """ Remove the record """
        user = kwargs['user']
        updatedUser = UpdateController.update(self, user.id, **kwargs)
        return {"token": BuildToken(updatedUser), "user": toJson(updatedUser)}