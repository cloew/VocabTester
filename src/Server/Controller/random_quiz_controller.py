from Data.language import Language
from Quiz.random_quiz_factory import RandomQuizFactory
from Server.helpers.json_factory import toJson

from auth_json_controller import AuthJSONController

class RandomQuizController(AuthJSONController):
    """ Controller to return a quiz built from random forms the user has learned """
    
    def __init__(self, formModel):
        """ Initialize the Quiz Controller """
        AuthJSONController.__init__(self)
        self.formModel = formModel
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the quiz to JSON """
        language = Language(id=languageId)
        quiz = RandomQuizFactory.buildQuiz(self.formModel, user, language)
        return {"quiz":toJson(quiz, user=user)}