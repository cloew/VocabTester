from ..auth import auth
from ..helpers.json_factory import toJson
from Data import ConceptManager, Language, Word

from sqlalchemy import func

class SearchController(auth.JSONController):
    """ Controller to return the words that match some provided text """
    
    def __init__(self):
        """ Initialize the Search Controller """
        auth.JSONController.__init__(self)
        self.conceptManager = ConceptManager(Word)
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the quiz to JSON """
        language = Language(id=languageId)
        conceptIds = [form.concept_id for form in Word.query.filter(func.lower(Word.text) == func.lower(json['text']))]
        pairs = self.conceptManager.getConceptPairs(conceptIds, user.nativeLanguage, language)
        return {"results":toJson(pairs, user=user)}