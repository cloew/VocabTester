from ..sampler import sample_at_most
from ..Ambiguity import AmbiguityHelper

import random

class OptionsQuestion:
    """ Represents a question with options in a Quiz """
    MAX_OPTIONS = 5
    
    def __init__(self, subject, allPairs):
        """ Initialize the question with the word to display, its matching translation and the other options """
        self.subject = subject
        self.queryWord = self.getQuestionForm(subject)
        self.answer = self.getOptionForm(subject)
        
        random.shuffle(allPairs)
        helper = AmbiguityHelper(allPairs)
        optionPairs = helper.getUnambiguousPairs(self.subject, self.MAX_OPTIONS)
        self.options = [self.getOptionForm(option) for option in optionPairs]
        
        random.shuffle(self.options)
        
    @property
    def answerIndex(self):
        """ Return the index of the answer to the question """
        return self.options.index(self.answer)
        
    def getQuestionForm(self, subject):
        """ Return the proper form of the subject pair to use in the question.
            Should be overridden by base class """
        return NotImplementedError
        
    def getOptionForm(self, option):
        """ Return the proper form of the option pair to use.
            Should be overridden by base class """
        raise NotImplementedError