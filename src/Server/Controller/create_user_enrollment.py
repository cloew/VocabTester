from Data.language_enrollment import LanguageEnrollment

from Server.decorators import requires_auth
from Server.helpers.json_factory import toJson

from kao_flask.ext.sqlalchemy import CreateController, RecordValueProvider

class CreateUserEnrollment(CreateController):
    """ Controller to create a user enrollment """
    
    def __init__(self):
        """ Initialize the Controller """
        CreateController.__init__(self, LanguageEnrollment, toJson, decorators=[requires_auth], 
                                  recordValueProvider=RecordValueProvider({'language': lambda value: ('language_id', value['id'])}))
    
    def performWithJSON(self, json=None, user=None):
        """ Convert the records to JSON """
        cleanJson = dict(json)
        cleanJson['user_id'] = user.id
        cleanJson['default'] = (len(user.languageEnrollments) == 0)
        return CreateController.performWithJSON(self, json=cleanJson)