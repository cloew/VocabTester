from Data.word import Word

from Quiz.answer_helper import Answer
from Server.Data.word_wrapper import WordWrapper

from auth_json_controller import AuthJSONController

class QuizAnswerController(AuthJSONController):
    """ Controller to create an answer for the quiz """
    
    def performWithJSON(self, wordlistId, user=None):
        """ Create an answer for the word's mastery """
        word = Word.query.filter_by(id=self.json['wordId']).first()
        Answer(word, self.json['correct'])
        return WordWrapper(word).toJSON()