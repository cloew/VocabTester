from Server.auth import auth
from Server.helpers import BuildLanguageContext
from Server.helpers.json_factory import toJson

from Data.Cache import BuildMasteryCache, LearnedCache
from Data.Query import ConceptListQueryHelper

class GetConceptLists(auth.JSONController):
    """ Controller to return the concept lists """
    
    def __init__(self, formInfo):
        """ Initialize the Concept Lists Controller """
        auth.JSONController.__init__(self)
        self.formInfo = formInfo
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the existing Concept Lists to JSON """
        languageContext = BuildLanguageContext(languageId, user)
        conceptListHelper = ConceptListQueryHelper(self.formInfo, user, self.formInfo.listModel.query, languageContext)
        masteryCache = BuildMasteryCache.ViaForms(conceptListHelper.foreignForms, self.formInfo, user)
        boundLists = conceptListHelper.bound_lists
        
        learnedCache = LearnedCache(user, self.formInfo)
        return {"lists":toJson([boundList for boundList in boundLists if len(boundList.concepts) > 0], user=user, learnedCache=learnedCache, masteryCache=masteryCache)}