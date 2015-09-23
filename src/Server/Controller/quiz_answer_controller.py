from ..auth import auth
from ..helpers.json_factory import toJson
from Data import Mastery

class QuizAnswerController(auth.JSONController):
    """ Controller to create an answer for the quiz """
    
    def performWithJSON(self, masteryId, json=None, user=None):
        """ Create an answer for the mastery """
        mastery = Mastery.query.filter_by(id=masteryId).first()
        mastery.addAnswer(json['correct'])
        
        if mastery.word_id is not None:
            user.tryToLearnWord(mastery.word)
        elif mastery.symbol_id is not None:
            user.tryToLearnSymbol(mastery.symbol)
        return {'rating':mastery.rating}