from ..auth import auth
from ..helpers.json_factory import toJson
from Data import Word, WordInfo
from Data.Cache import LearnedCache

class LearnWordController(auth.JSONController):
    """ Controller to mark a word as learned """
    
    def performWithJSON(self, wordId, json=None, user=None):
        """ Mark a word as learned by the current user """
        word = Word.query.filter_by(id=wordId).first()
        user.tryToLearnWord(word)
        learnedCache = LearnedCache(user, WordInfo)
        return {"word":toJson(word, user=user, learnedCache=learnedCache)}