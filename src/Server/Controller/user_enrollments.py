from ..auth import auth
from ..helpers.json_factory import toJson

class UserEnrollments(auth.JSONController):
    """ Controller to return the languages the user has enrolled in """
    
    def performWithJSON(self, json=None, user=None):
        """ Convert the User's enrollments to Json """
        return {'enrollments':toJson(user.languageEnrollments)}