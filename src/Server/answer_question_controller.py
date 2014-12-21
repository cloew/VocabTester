from Server.Question.results_wrapper_factory import GetResultsWrapper

from Data.temp_data import GetQuiz

from kao_flask.controllers.json_controller import JSONController

class AnswerQuestionController(JSONController):
    """ Controller to answer a question """
    
    def performWithJSON(self, wordlistId):
        """ Convert the quiz to JSON """
        quizzer = GetQuiz()
        quizzer.answer(self.json["answer"])
        results = quizzer.latestResults
        return {"results":GetResultsWrapper(results).toJSON()}