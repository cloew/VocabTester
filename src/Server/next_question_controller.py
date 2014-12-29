from quizzer_wrapper import QuizzerWrapper

from Data.temp_data import GetQuiz

from kao_flask.controllers.json_controller import JSONController

class NextQuestionController(JSONController):
    """ Controller to return the quiz set to the next question """
    
    def performWithJSON(self, wordlistId):
        """ Convert the quiz to JSON """
        quizzer = GetQuiz()
        return {"quiz":QuizzerWrapper(quizzer).toJSON()}