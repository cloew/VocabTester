from ..auth import auth
from ..helpers import BuildLanguageContext
from ..helpers.json_factory import toJson

from Data import Word
from Data.Cache import BuildMasteryCache
from Data.Query import PrequeriedFormsHelper

class LearnedConceptsController(auth.JSONController):
    """ Controller to return the concepts learned in the appropriate form """
    
    def __init__(self, formInfo):
        """ Initialize the Quiz Controller """
        auth.JSONController.__init__(self)
        self.formInfo = formInfo
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the quiz to JSON """
        languageContext = BuildLanguageContext(languageId, user)
        learnedForms = user.getLearnedFor(self.formInfo.formModel, languageContext.foreign)
        learnedFormsHelper = PrequeriedFormsHelper(learnedForms, self.formInfo, languageContext)
        
        pairs = learnedFormsHelper.getConceptPairs()
        masteryCache = BuildMasteryCache.ViaPairs(pairs, self.formInfo, user)
        
        return {"concepts":toJson(pairs, user=user, masteryCache=masteryCache), "isWords":self.formInfo.formModel is Word}