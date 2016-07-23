from Server.auth import auth
from Server.helpers import BuildLearningContext
from Server.helpers.json_factory import toJson

from Data import Word
from Data.Cache import BuildMasteryCache, LearnedCache
from Data.Query import PrequeriedFormsHelper

class GetLearnedConcepts(auth.JSONController):
    """ Controller to return the concepts learned in the appropriate form """
    
    def __init__(self, formInfo):
        """ Initialize the Quiz Controller """
        auth.JSONController.__init__(self)
        self.formInfo = formInfo
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the quiz to JSON """
        learningContext = BuildLearningContext(languageId, user)
        languageContext = learningContext.languageContext
        
        learnedForms = user.getLearnedFor(self.formInfo, languageContext.foreign)
        learnedFormsHelper = PrequeriedFormsHelper(learnedForms, self.formInfo, languageContext)
        
        pairs = learnedFormsHelper.getConceptPairs()
        masteryCache = BuildMasteryCache.ViaPairs(pairs, self.formInfo, user)
        learnedCache = LearnedCache(user, self.formInfo)
        
        return {"concepts":toJson(pairs, user=user, learnedCache=learnedCache, masteryCache=masteryCache), "isWords":self.formInfo.formModel is Word}