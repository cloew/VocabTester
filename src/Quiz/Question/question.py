from Quiz.sampler import sample_at_most
from options_finder import OptionsFinder

import random

class Question:
    """ Represents a question in a Quiz """
    NUM_WRONG_ANSWERS = 4
    
    def __init__(self, subject, allPairs):
        """ Initialize the question with the word to display, its matching translation and the other options """
        self.subject = subject
        self.queryWord = self.getQuestionForm(subject)
        self.answer = self.getOptionForm(subject)
        
        optionFinder = OptionsFinder(subject, allPairs)
        self.otherOptions = [self.getOptionForm(option) for option in optionFinder.options]
        
        self.options = [self.answer] + sample_at_most(self.otherOptions, self.NUM_WRONG_ANSWERS)
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