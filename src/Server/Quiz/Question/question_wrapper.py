from Server.Data.concept_pair_wrapper import ConceptPairWrapper
from Server.Data.word_wrapper import GetWordListJSON, WordWrapper

class QuestionWrapper:
    """ Converts a Question to JSON """
    
    def __init__(self, question):
        """ Initialize the question wrapper """
        self.question = question
        
    def toJSON(self, user):
        """ Convert the word list to JSON """
        return {"subject":ConceptPairWrapper(self.question.subject).toJSON(user),
                "queryWord":WordWrapper(self.question.queryWord).toJSON(user),
                "options":GetWordListJSON(self.question.options, user),
                "answerIndex":self.question.answerIndex}