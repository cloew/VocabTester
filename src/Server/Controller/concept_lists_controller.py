from .auth_json_controller import AuthJSONController
from Data.language import Language
from Data.user_concept_list import UserConceptList

from Server.helpers.json_factory import toJson

class ConceptListsController(AuthJSONController):
    """ Controller to return the concept lists """
    
    def __init__(self, listModel):
        """ Initialize the Concept Lists Controller """
        AuthJSONController.__init__(self)
        self.listModel = listModel
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the existing Concept Lists to JSON """
        language = Language(id=languageId)
        conceptLists = self.listModel.query.all()
        userLists = [UserConceptList(conceptList, user, language) for conceptList in conceptLists]
        return {"lists":toJson([userList for userList in userLists if len(userList.concepts) > 0], user=user)}