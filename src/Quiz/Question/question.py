import random

class Question:
    """ Represents a question in a Quiz """
    NUM_WRONG_ANSWERS = 4
    
    def __init__(self, subject, queryWord, answer, otherOptions):
        """ Initialize the question with the word to display, its matching translation and the other options """
        self.subject = subject
        self.queryWord = queryWord
        self.answer = answer
        self.otherOptions = otherOptions
        
        self.options = [self.answer] + random.sample(self.otherOptions, self.numberOfWrongAnswers)
        random.shuffle(self.options)
        
    @property
    def numberOfWrongAnswers(self):
        """ Returns the number of wrong answers for this question """
        return min(len(self.otherOptions), self.NUM_WRONG_ANSWERS)
        
    @property
    def answerIndex(self):
        """ Return the index of the answer to the question """
        return self.options.index(self.answer)