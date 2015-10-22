from .native_options_question import NativeOptionsQuestion
from .foreign_options_question import ForeignOptionsQuestion
from .options_question_builder import OptionsQuestionBuilder
from .prompt_question_builder import PromptQuestionBuilder

from ..ratio_picker import RatioPicker

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
                     
    def buildQuestions(self, pairs, masteryCache):
        """ Build the questions for use in the quiz """
        questions = []
        for mastery, conceptPairs in groupby(pairs, lambda pair: masteryCache[pair.foreign.id].answerRating):
            if mastery in self.optionsRange:
                questions += self.optionsQuestionBuilder.buildQuestions(list(conceptPairs), pairs)
            if mastery in self.promptRange:
                questions += self.promptQuestionBuilder.buildQuestions(list(conceptPairs))
        return questions
    
QuestionFactory = QuestionFactory()