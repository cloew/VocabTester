from ..auth import auth
from ..helpers.json_factory import toJson
from Data import Language
from Quiz import RandomQuizFactory

class RandomQuizController(auth.JSONController):
    """ Controller to return a quiz built from random forms the user has learned """
    
    def __init__(self, formModel):
        """ Initialize the Quiz Controller """
        auth.JSONController.__init__(self)
        self.formModel = formModel
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the quiz to JSON """
        language = Language(id=languageId)
        quiz = RandomQuizFactory.buildQuiz(self.formModel, user, language)
        return {"quiz":toJson(quiz, user=user)}