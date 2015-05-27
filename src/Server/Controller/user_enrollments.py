from auth_json_controller import AuthJSONController
from Server.helpers.json_factory import toJson

class UserEnrollments(AuthJSONController):
    """ Controller to return the languages the user has enrolled in """
    
    def performWithJSON(self, json=None, user=None):
        """ Convert the User's enrollments to Json """
        return {'enrollments':toJson(user.languageEnrollments)}