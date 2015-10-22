from ..auth import auth
from ..helpers import BuildLanguageContext
from ..helpers.json_factory import toJson

from Data import Word
from Data.Cache import MasteryCache
from Data.Query import PrequeriedFormsHelper

class LearnedConceptsController(auth.JSONController):
    """ Controller to return the concepts learned in the appropriate form """
    
    def __init__(self, formModel):
        """ Initialize the Quiz Controller """
        auth.JSONController.__init__(self)
        self.formModel = formModel
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the quiz to JSON """
        languageContext = BuildLanguageContext(languageId, user)
        learnedForms = user.getLearnedFor(self.formModel, languageContext.foreign)
        learnedFormsHelper = PrequeriedFormsHelper(learnedForms, self.formModel, languageContext)
        
        pairs = learnedFormsHelper.getConceptPairs()
        masteryCache = MasteryCache([pair.foreign for pair in pairs], self.formModel, user)
        
        return {"concepts":toJson(pairs, user=user, masteryCache=masteryCache), "isWords":self.formModel is Word}