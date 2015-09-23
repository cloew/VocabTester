from ..auth import auth
from ..helpers.json_factory import toJson
from Data import Word

class LearnWordController(auth.JSONController):
    """ Controller to mark a word as learned """
    
    def performWithJSON(self, wordId, json=None, user=None):
        """ Mark a word as learned by the current user """
        word = Word.query.filter_by(id=wordId).first()
        user.tryToLearnWord(word)
        return {"word":toJson(word, user=user)}