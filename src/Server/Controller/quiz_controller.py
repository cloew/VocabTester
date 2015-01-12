from Server.Quiz.quiz_wrapper import QuizWrapper

from Data.word_list import WordList
import Data.concept_manager as cm

from Quiz.quiz import Quiz

from kao_flask.controllers.json_controller import JSONController

class QuizController(JSONController):
    """ Controller to return the quiz """
    
    def performWithJSON(self, wordlistId):
        """ Convert the quiz to JSON """
        wordList = WordList.query.filter_by(id=wordlistId).first()
        quiz = Quiz(wordList, cm)
        return {"quiz":QuizWrapper(quiz).toJSON()}