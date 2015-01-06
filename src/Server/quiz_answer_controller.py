from Data.word import Word

from Quiz.answer_helper import Answer

from kao_flask.controllers.json_controller import JSONController

class QuizAnswerController(JSONController):
    """ Controller to create an answer for the quiz """
    
    def performWithJSON(self, wordlistId):
        """ Create an answer for the word's mastery """
        word = Word.query().filter_by(id=self.json.wordId).first()
        Answer(word, self.json.correct)