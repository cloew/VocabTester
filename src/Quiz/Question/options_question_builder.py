from .native_options_question import NativeOptionsQuestion
from .foreign_options_question import ForeignOptionsQuestion
from ..ratio_picker import RatioPicker

import random

class OptionsQuestionBuilder:
    """ Helper class to construct Options Question Builder """
    questionClassRatio = RatioPicker([(ForeignOptionsQuestion, .5),
                                      (NativeOptionsQuestion, .5)])
                     
    def buildQuestions(self, pairs, allPairs):
        """ Build the questions for use in the quiz """
        if len(pairs) == 0:
            return []
        random.shuffle(pairs)
        questionClasses = self.getQuestionClasses(pairs)
        return [questionClass(pair, allPairs) for pair, questionClass in zip(pairs, questionClasses)]
    
    def getQuestionClasses(self, pairs):
        """ Return the question classes """
        questionClasses = self.questionClassRatio.getResults(len(pairs))
        random.shuffle(questionClasses)
        return questionClasses