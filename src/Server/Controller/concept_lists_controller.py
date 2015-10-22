from ..auth import auth
from ..helpers import BuildLanguageContext
from ..helpers.json_factory import toJson

from Data.Cache import BuildMasteryCache
from Data.Query import ConceptListQueryHelper

class ConceptListsController(auth.JSONController):
    """ Controller to return the concept lists """
    
    def __init__(self, formInfo):
        """ Initialize the Concept Lists Controller """
        auth.JSONController.__init__(self)
        self.formInfo = formInfo
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the existing Concept Lists to JSON """
        languageContext = BuildLanguageContext(languageId, user)
        conceptListHelper = ConceptListQueryHelper(self.formInfo, self.formInfo.listModel.query, languageContext)
        masteryCache = BuildMasteryCache.ViaForms(conceptListHelper.foreignForms, self.formInfo, user)
        userLists = conceptListHelper.buildUserLists(user)
        
        return {"lists":toJson([userList for userList in userLists if len(userList.concepts) > 0], user=user, masteryCache=masteryCache)}