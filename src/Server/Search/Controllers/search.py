from Server.auth import auth
from Server.helpers import BuildLanguageContext
from Server.helpers.json_factory import toJson

from Data import Language, Word, WordInfo
from Data.Cache import BuildMasteryCache, LearnedCache
from Data.Query import PrequeriedFormsHelper

from sqlalchemy import func

class Search(auth.JSONController):
    """ Controller to return the words that match some provided text """
    
    def __init__(self):
        """ Initialize the Search Controller """
        auth.JSONController.__init__(self)
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the quiz to JSON """
        languageContext = BuildLanguageContext(languageId, user)
        uniqueForms = self.getUniqueConcepts(json['text'], languageContext)
        matchingHelper = PrequeriedFormsHelper(uniqueForms, WordInfo, languageContext)
        
        pairs = matchingHelper.getConceptPairs()
        masteryCache = BuildMasteryCache.ViaPairs(pairs, WordInfo, user)
        learnedCache = LearnedCache(user, WordInfo)
        
        return {"results":toJson(pairs, user=user, learnedCache=learnedCache, masteryCache=masteryCache)}
        
    def getUniqueConcepts(self, text, languageContext):
        """ Return the Unique Concept Forms """
        matchingForms = Word.query.filter(func.lower(Word.text) == func.lower(text)).filter(Word.language_id.in_([l.id for l in languageContext])).all()
        
        conceptIds = set()
        uniqueForms = []
        for form in matchingForms:
            if form.concept_id not in conceptIds:
                conceptIds.add(form.concept_id)
                uniqueForms.append(form)
        return uniqueForms
        