from .subject import Subject
from ..sampler import sample_at_most
from ..Ambiguity import AmbiguityHelper

from proxy_attrs import proxy_for

import random

@proxy_for('subject', ['answerForm'])
class OptionsQuestion:
    """ Represents a question with options in a Quiz """
    MAX_OPTIONS = 5
    
    def __init__(self, subjectPair, allPairs, *, subjectForm, optionsForm):
        """ Initialize the question with the word to display, its matching translation and the other options """
        self.subject = Subject(subjectPair, subjectForm)
        
        random.shuffle(allPairs)
        helper = AmbiguityHelper(allPairs)
        optionPairs = helper.getUnambiguousPairs(subjectPair, self.MAX_OPTIONS)
        self.options = [optionsForm(option) for option in optionPairs]
        
        random.shuffle(self.options)
        
    @property
    def answerIndex(self):
        """ Return the index of the answer to the question """
        return self.options.index(self.answerForm)