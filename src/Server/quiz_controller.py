from quizzer_wrapper import QuizzerWrapper

from Data.concept_manager import ConceptManager
from Data.word_list import WordList

from Quiz.quiz import Quiz
from Quiz.quizzer import Quizzer

from kao_flask.controllers.json_controller import JSONController

class QuizController(JSONController):
    """ Controller to return the quiz """
    cm = ConceptManager(["resources/days_of_week_english.json", "resources/days_of_week_japanese.json"])
    
    def performWithJSON(self, wordlistId):
        """ Convert the quiz to JSON """
        wordList = WordList("Days of the Week", range(1,8), "English", "Japanese")
        quizzer = Quizzer(Quiz(wordList, self.cm))
        return {"quiz":QuizzerWrapper(quizzer).toJSON()}