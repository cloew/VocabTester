from quizzer_wrapper import QuizzerWrapper

from Data.word_list import WordList
import Data.concept_manager as cm

from kao_flask.controllers.json_controller import JSONController

class QuizController(JSONController):
    """ Controller to return the quiz """
    
    def performWithJSON(self, wordListId):
        """ Convert the quiz to JSON """
        wordList = WordList.query.filter_by(id=wordListId).first()
        quizzer = Quizzer(Quiz(wordList, cm))
        return {"quiz":QuizzerWrapper(quizzer).toJSON()}