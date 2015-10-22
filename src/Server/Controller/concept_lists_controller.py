from ..auth import auth
from ..helpers import BuildLanguageContext
from ..helpers.json_factory import toJson
from Data.Cache import MasteryCache
from Data.Query import ConceptListQueryHelper

class ConceptListsController(auth.JSONController):
    """ Controller to return the concept lists """
    
    def __init__(self, listModel):
        """ Initialize the Concept Lists Controller """
        auth.JSONController.__init__(self)
        self.listModel = listModel
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the existing Concept Lists to JSON """
        languageContext = BuildLanguageContext(languageId, user)
        conceptListHelper = ConceptListQueryHelper(self.listModel, self.listModel.query, languageContext)
        masteryCache = MasteryCache(conceptListHelper.foreignForms, self.listModel.conceptFormCls, user)
        userLists = conceptListHelper.buildUserLists(user)
        
        return {"lists":toJson([userList for userList in userLists if len(userList.concepts) > 0], user=user, masteryCache=masteryCache)}