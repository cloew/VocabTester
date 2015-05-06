from native_options_question import NativeOptionsQuestion
from foreign_options_question import ForeignOptionsQuestion

from Quiz.ratio_picker import RatioPicker

from .options_question_builder import OptionsQuestionBuilder
import random

class QuestionFactory:
    """ Constructs Questions """
    questionClassRatio = RatioPicker([(ForeignOptionsQuestion, .5),
                                      (NativeOptionsQuestion, .5)])
                                      
    def __init__(self):
        """ Initialize the question factory with the builders for each question type """
        self.optionsQuestionBuilder = OptionsQuestionBuilder()
                     
    def buildQuestions(self, pairs):
        """ Build the questions for use in the quiz """
        return self.optionsQuestionBuilder.buildQuestions(pairs)
    
    def getQuestionClasses(self, pairs):
        """ Return the question classes """
        questionClasses = self.questionClassRatio.getResults(len(pairs))
        random.shuffle(questionClasses)
        return questionClasses
    
QuestionFactory = QuestionFactory()