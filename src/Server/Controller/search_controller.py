from ..auth import auth
from ..helpers.json_factory import toJson
from Data import Language, Word
from Data.Query import PrequeriedFormsHelper

from sqlalchemy import func

class SearchController(auth.JSONController):
    """ Controller to return the words that match some provided text """
    
    def __init__(self):
        """ Initialize the Search Controller """
        auth.JSONController.__init__(self)
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the quiz to JSON """
        language = Language(id=languageId)
        matchingForms = Word.query.filter(func.lower(Word.text) == func.lower(json['text'])).all()
        mathcingHelper = PrequeriedFormsHelper(matchingForms, Word, foreign=language, native=user.nativeLanguage)
        pairs = mathcingHelper.getConceptPairs()
        return {"results":toJson(pairs, user=user)}