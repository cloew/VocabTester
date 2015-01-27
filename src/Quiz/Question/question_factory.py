from native_options_question import NativeOptionsQuestion
from foreign_options_question import ForeignOptionsQuestion

from Quiz.ratio_picker import RatioPicker

import random

class QuestionFactory:
    """ Constructs Questions """
    questionClassRatio = RatioPicker([(ForeignOptionsQuestion, .5),
                                      (NativeOptionsQuestion, .5)])
                     
    def buildQuestions(self, pairs):
        """ Build the questions for use in the quiz """
        random.shuffle(pairs)
        questionClasses = self.getQuestionClasses(pairs)
        
        setOfPairs = set(pairs)
        return [questionClass(pair, setOfPairs) for pair, questionClass in zip(pairs, questionClasses)]
    
    def getQuestionClasses(self, pairs):
        """ Return the question classes """
        questionClasses = self.questionClassRatio.getResults(len(pairs))
        random.shuffle(questionClasses)
        return questionClasses
    
QuestionFactory = QuestionFactory()