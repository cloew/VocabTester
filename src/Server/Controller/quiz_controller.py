from ..auth import auth
from ..helpers.json_factory import toJson
from Data import Language
from Quiz.quiz import Quiz

class QuizController(auth.JSONController):
    """ Controller to return the quiz """
    
    def __init__(self, listModel):
        """ Initialize the Quiz Controller """
        auth.JSONController.__init__(self)
        self.listModel = listModel
    
    def performWithJSON(self, languageId, listId, json=None, user=None):
        """ Convert the quiz to JSON """
        language = Language(id=languageId)
        conceptList = self.listModel.query.filter_by(id=listId).first()
        pairs = conceptList.getConceptPairs(user.nativeLanguage, language)
        quiz = Quiz(conceptList.name, pairs, user)
        return {"quiz":toJson(quiz, user=user)}