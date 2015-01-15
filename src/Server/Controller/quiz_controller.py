from Data.word_list import WordList
import Data.concept_manager as cm

from Quiz.quiz import Quiz
from Server.Data.json_factory import toJson

from auth_json_controller import AuthJSONController

class QuizController(AuthJSONController):
    """ Controller to return the quiz """
    
    def performWithJSON(self, wordlistId, json=None, user=None):
        """ Convert the quiz to JSON """
        wordList = WordList.query.filter_by(id=wordlistId).first()
        quiz = Quiz(wordList, cm)
        return {"quiz":toJson(quiz, user=user)}