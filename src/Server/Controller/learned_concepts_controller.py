from Data.concept_manager import ConceptManager
from Server.helpers.json_factory import toJson

from auth_json_controller import AuthJSONController

class LearnedConceptsController(AuthJSONController):
    """ Controller to return the concepts learned in the appropriate form """
    
    def __init__(self, formModel):
        """ Initialize the Quiz Controller """
        AuthJSONController.__init__(self)
        self.formModel = formModel
        self.conceptManager = ConceptManager(formModel)
    
    def performWithJSON(self, json=None, user=None):
        """ Convert the quiz to JSON """
        learnedForms = user.getLearnedFor(self.formModel)
        conceptIds = [form.concept_id for form in learnedForms]
        pairs = self.conceptManager.getConceptPairs(conceptIds, user)
        return {"concepts":toJson(pairs, user=user)}