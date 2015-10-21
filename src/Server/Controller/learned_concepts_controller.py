from ..auth import auth
from ..helpers.json_factory import toJson
from Data import Language, Word
from Data.Query import LearnedFormsQueryHelper

class LearnedConceptsController(auth.JSONController):
    """ Controller to return the concepts learned in the appropriate form """
    
    def __init__(self, formModel):
        """ Initialize the Quiz Controller """
        auth.JSONController.__init__(self)
        self.formModel = formModel
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the quiz to JSON """
        language = Language(id=languageId)
        learnedFormsHelper = LearnedFormsQueryHelper(user, self.formModel, foreign=language)
        pairs = learnedFormsHelper.getConceptPairs()
        return {"concepts":toJson(pairs, user=user), "isWords":self.formModel is Word}