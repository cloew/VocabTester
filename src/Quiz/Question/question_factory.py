from native_options_question import NativeOptionsQuestion
from foreign_options_question import ForeignOptionsQuestion

from Quiz.ratio_picker import RatioPicker

from .options_question_builder import OptionsQuestionBuilder
from .prompt_question_builder import PromptQuestionBuilder

from itertools import groupby
import random

class QuestionFactory:
    """ Constructs Questions """
                                      
    def __init__(self):
        """ Initialize the question factory with the builders for each question type """
        self.optionsQuestionBuilder = OptionsQuestionBuilder()
        self.promptQuestionBuilder = PromptQuestionBuilder()
        
        self.optionsRange = range(0,4)
        self.promptRange = range(4,6)
                     
    def buildQuestions(self, pairs, user):
        """ Build the questions for use in the quiz """
        questions = []
        for mastery, conceptPairs in groupby(pairs, lambda pair: pair.foreign.getMastery(user).rating):
            if mastery in sef.optionsRange:
                questions += self.optionsQuestionBuilder.buildQuestions(conceptPairs)
            if mastery in sef.promptRange:
                questions += self.promptQuestionBuilder.buildQuestions(conceptPairs)
        return questions
    
QuestionFactory = QuestionFactory()