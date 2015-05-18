from Data.language import Language
from Quiz.quiz import Quiz
from Server.helpers.json_factory import toJson

from auth_json_controller import AuthJSONController

class QuizController(AuthJSONController):
    """ Controller to return the quiz """
    
    def __init__(self, listModel):
        """ Initialize the Quiz Controller """
        AuthJSONController.__init__(self)
        self.listModel = listModel
    
    def performWithJSON(self, languageId, listId, json=None, user=None):
        """ Convert the quiz to JSON """
        language = Language(id=languageId)
        conceptList = self.listModel.query.filter_by(id=listId).first()
        pairs = conceptList.getConceptPairs(user.nativeLanguage, language)
        quiz = Quiz(conceptList.name, pairs, user)
        return {"quiz":toJson(quiz, user=user)}