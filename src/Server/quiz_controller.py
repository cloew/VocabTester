from quizzer_wrapper import QuizzerWrapper

from Data.temp_data import BuildQuiz

from kao_flask.controllers.json_controller import JSONController

class QuizController(JSONController):
    """ Controller to return the quiz """
    
    def performWithJSON(self, wordlistId):
        """ Convert the quiz to JSON """
        quizzer = BuildQuiz()
        return {"quiz":QuizzerWrapper(quizzer).toJSON()}