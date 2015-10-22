from Server.auth import auth
from Server.helpers import BuildLanguageContext
from Server.helpers.json_factory import toJson

from Data import Language
from Quiz import RandomQuizFactory

class GetRandomQuiz(auth.JSONController):
    """ Controller to return a quiz built from random forms the user has learned """
    
    def __init__(self, formModel):
        """ Initialize the Quiz Controller """
        auth.JSONController.__init__(self)
        self.formModel = formModel
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the quiz to JSON """
        languageContext = BuildLanguageContext(languageId, user)
        quiz, masteryCache = RandomQuizFactory.buildQuiz(self.formModel, user, languageContext)
        return {"quiz":toJson(quiz, user=user, masteryCache=masteryCache)}