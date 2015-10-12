from Server.auth import auth
from Server.helpers.json_factory import toJson

from Data import Mastery
from Quiz import Graders

class AnswerQuestion(auth.JSONController):
    """ Controller to create an answer for a quiz """
    
    def performWithJSON(self, masteryId, json=None, user=None):
        """ Create an answer for the mastery """
        result = self.grade(json)
        
        mastery = Mastery.query.filter_by(id=masteryId).first()
        mastery.addAnswer(result.correct)
        
        if mastery.word_id is not None:
            user.tryToLearnWord(mastery.word)
        elif mastery.symbol_id is not None:
            user.tryToLearnSymbol(mastery.symbol)
        return {'results':toJson(result),
                'rating':mastery.rating}
        
    def grade(self, json):
        """ Return whether the question was answered correctly """
        grader = Graders[json['type']]
        return grader.grade(json['guess'], json['answer'])