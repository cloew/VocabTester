from Server.auth import auth
from Server.helpers import BuildLearningContext
from Server.helpers.json_factory import toJson

from Data import Language
from Data.Cache import LearnedCache
from Quiz import RandomQuizFactory

class GetRandomQuiz(auth.JSONController):
    """ Controller to return a quiz built from random forms the user has learned """
    
    def __init__(self, formInfo):
        """ Initialize the Quiz Controller """
        auth.JSONController.__init__(self)
        self.formInfo = formInfo
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the quiz to JSON """
        learningContext = BuildLearningContext(languageId, user)
        languageContext = learningContext.languageContext
        
        quiz, masteryCache = RandomQuizFactory.buildQuiz(self.formInfo, user, languageContext)
        learnedCache = LearnedCache(user, self.formInfo)
        return {"quiz":toJson(quiz, user=user, learnedCache=learnedCache, masteryCache=masteryCache)}