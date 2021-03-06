from Server.auth import auth
from Server.helpers.json_factory import toJson

from Data import Mastery, SymbolInfo, WordInfo
from Data.Cache import LearnedCache
from Quiz import Graders

class AnswerQuestion(auth.JSONController):
    """ Controller to create an answer for a quiz """
    
    def performWithJSON(self, masteryId, json=None, user=None):
        """ Create an answer for the mastery """
        result = self.grade(json)
        
        mastery = Mastery.query.filter_by(id=masteryId).first()
        mastery.addAnswer(result.correct)
        
        formInfo = WordInfo if mastery.word_id is not None else SymbolInfo
        learnedCache = LearnedCache(user, formInfo)
        user.tryToLearn(mastery.form, formInfo, learnedCache)
        
        return {'results':toJson(result),
                'rating':mastery.rating}
        
    def grade(self, json):
        """ Return whether the question was answered correctly """
        grader = Graders[json['type']]
        return grader.grade(json['guess'], json['answer'])