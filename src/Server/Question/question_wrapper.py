from Server.word_wrapper import GetWordListJSON, WordWrapper

class QuestionWrapper:
    """ Converts a Question to JSON """
    
    def __init__(self, question):
        """ Initialize the question wrapper """
        self.question = question
        
    def toJSON(self):
        """ Convert the word list to JSON """
        return {"word":WordWrapper(self.question.word).toJSON(),
                "options":GetWordListJSON(self.question.options)}