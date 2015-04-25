from Data.concept_manager import ConceptManager
from Data.word import Word

from Server.helpers.admin_json_factory import toJson

from auth_json_controller import AuthJSONController

class ConceptsController(AuthJSONController):
    """ Controller to return the concepts learned in the appropriate form """
    
    def __init__(self, formModel):
        """ Initialize the Quiz Controller """
        AuthJSONController.__init__(self)
        self.formModel = formModel
        self.conceptManager = ConceptManager(formModel)
    
    def performWithJSON(self, json=None, user=None):
        """ Convert the quiz to JSON """
        conceptIds = [form.concept_id for form in self.formModel.query.all()]
        pairs = self.conceptManager.getConceptPairs(conceptIds, user)
        return {"concepts":toJson(pairs), "isWords":self.formModel is Word}