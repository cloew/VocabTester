from Server.word_wrapper import GetWordListJSON, WordWrapper

class QuestionWrapper:
    """ Converts a Question to JSON """
    
    def __init__(self, question):
        """ Initialize the question wrapper """
        self.question = question
        
    def toJSON(self):
        """ Convert the word list to JSON """
        return {"subject":WordWrapper(self.question.subject).toJSON(),
                "queryWord":WordWrapper(self.question.queryWord).toJSON(),
                "options":GetWordListJSON(self.question.options),
                "answerIndex":self.question.answerIndex}