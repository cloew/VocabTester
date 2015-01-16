from Quiz.quiz import Quiz
from Server.helpers.json_factory import toJson

from auth_json_controller import AuthJSONController

class QuizController(AuthJSONController):
    """ Controller to return the quiz """
    
    def __init__(self, listModel):
        """ Initialize the Quiz Controller """
        AuthJSONController.__init__(self)
        self.listModel = listModel
    
    def performWithJSON(self, listId, json=None, user=None):
        """ Convert the quiz to JSON """
        conceptList = self.listModel.query.filter_by(id=listId).first()
        quiz = Quiz(conceptList, user)
        return {"quiz":toJson(quiz, user=user)}