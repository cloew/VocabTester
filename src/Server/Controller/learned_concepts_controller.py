from .auth_json_controller import AuthJSONController

from Data.concept_manager import ConceptManager
from Data.language import Language
from Data.word import Word

from Server.helpers.json_factory import toJson

class LearnedConceptsController(AuthJSONController):
    """ Controller to return the concepts learned in the appropriate form """
    
    def __init__(self, formModel):
        """ Initialize the Quiz Controller """
        AuthJSONController.__init__(self)
        self.formModel = formModel
        self.conceptManager = ConceptManager(formModel)
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the quiz to JSON """
        language = Language(id=languageId)
        learnedForms = user.getLearnedFor(self.formModel, language)
        conceptIds = [form.concept_id for form in learnedForms]
        pairs = self.conceptManager.getConceptPairs(conceptIds, user.nativeLanguage, language)
        return {"concepts":toJson(pairs, user=user), "isWords":self.formModel is Word}