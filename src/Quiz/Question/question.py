from Quiz.sampler import sample_at_most
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
        
        self.options = [self.answer] + sample_at_most(self.otherOptions, self.NUM_WRONG_ANSWERS)
        random.shuffle(self.options)
        
    @property
    def answerIndex(self):
        """ Return the index of the answer to the question """
        return self.options.index(self.answer)