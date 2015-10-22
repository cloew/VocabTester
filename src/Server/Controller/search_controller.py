from ..auth import auth
from ..helpers import BuildLanguageContext
from ..helpers.json_factory import toJson

from Data import Language, Word, WordInfo
from Data.Cache import BuildMasteryCache
from Data.Query import PrequeriedFormsHelper

from sqlalchemy import func

class SearchController(auth.JSONController):
    """ Controller to return the words that match some provided text """
    
    def __init__(self):
        """ Initialize the Search Controller """
        auth.JSONController.__init__(self)
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the quiz to JSON """
        languageContext = BuildLanguageContext(languageId, user)
        matchingForms = Word.query.filter(func.lower(Word.text) == func.lower(json['text'])).all()
        matchingHelper = PrequeriedFormsHelper(matchingForms, WordInfo, languageContext)
        
        pairs = matchingHelper.getConceptPairs()
        masteryCache = BuildMasteryCache.ViaPairs(pairs, WordInfo, user)
        
        return {"results":toJson(pairs, user=user, masteryCache=masteryCache)}