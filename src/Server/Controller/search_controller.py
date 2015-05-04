from Data.concept_manager import ConceptManager
from Data.word import Word

from Server.helpers.json_factory import toJson

from auth_json_controller import AuthJSONController

class SearchController(AuthJSONController):
    """ Controller to return the words that match some provided text """
    
    def __init__(self):
        """ Initialize the Search Controller """
        AuthJSONController.__init__(self)
        self.conceptManager = ConceptManager(Word)
    
    def performWithJSON(self, json=None, user=None):
        """ Convert the quiz to JSON """
        conceptIds = [form.concept_id for form in Word.query.filter_by(text=json['text'])]
        pairs = self.conceptManager.getConceptPairs(conceptIds, user)
        return {"results":toJson(pairs, user=user)}