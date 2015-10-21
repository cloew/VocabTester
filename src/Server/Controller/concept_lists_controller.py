from ..auth import auth
from ..helpers.json_factory import toJson
from Data import ConceptManager, Language, UserConceptList
from Data.Cache import ConceptFormCache
from Data.Query import ConceptListQueryHelper

from sqlalchemy.orm import subqueryload
import itertools

class ConceptListsController(auth.JSONController):
    """ Controller to return the concept lists """
    
    def __init__(self, listModel):
        """ Initialize the Concept Lists Controller """
        auth.JSONController.__init__(self)
        self.listModel = listModel
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the existing Concept Lists to JSON """
        foreignLanguage = Language(id=languageId)
        conceptListHelper = ConceptListQueryHelper(self.listModel, self.listModel.query, native=user.nativeLanguage, foreign=foreignLanguage)
        userLists = conceptListHelper.buildUserLists(user)
        return {"lists":toJson([userList for userList in userLists if len(userList.concepts) > 0], user=user)}