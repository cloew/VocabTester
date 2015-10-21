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
        foreignLanguage = Language(id=languageId)
        nativeLanguage = Language(id=user.native_language_id)
        
        matchingForms = Word.query.filter(func.lower(Word.text) == func.lower(json['text'])).all()
        matchingHelper = PrequeriedFormsHelper(matchingForms, Word, foreign=foreignLanguage, native=nativeLanguage)
        pairs = matchingHelper.getConceptPairs()
        return {"results":toJson(pairs, user=user)}