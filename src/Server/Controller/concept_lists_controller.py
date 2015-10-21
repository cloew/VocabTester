from ..auth import auth
from ..helpers.json_factory import toJson
from Data import Language
from Data.Query import ConceptListQueryHelper

class ConceptListsController(auth.JSONController):
    """ Controller to return the concept lists """
    
    def __init__(self, listModel):
        """ Initialize the Concept Lists Controller """
        auth.JSONController.__init__(self)
        self.listModel = listModel
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the existing Concept Lists to JSON """
        foreignLanguage = Language(id=languageId)
        nativeLanguage = Language(id=user.native_language_id)
        
        conceptListHelper = ConceptListQueryHelper(self.listModel, self.listModel.query, native=nativeLanguage, foreign=foreignLanguage)
        userLists = conceptListHelper.buildUserLists(user)
        return {"lists":toJson([userList for userList in userLists if len(userList.concepts) > 0], user=user)}