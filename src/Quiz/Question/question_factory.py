from .options_question_builder import OptionsQuestionBuilder
from .prompt_question_builder import PromptQuestionBuilder

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
        optionsPairs = []
        promptPairs = []
        
        for pair in pairs:
            mastery = masteryCache[pair.foreign.id].answerRating
            if mastery in self.optionsRange:
                optionsPairs.append(pair)
            if mastery in self.promptRange:
                promptPairs.append(pair)
                
        questions.extend(self.optionsQuestionBuilder.buildQuestions(optionsPairs, pairs))
        questions.extend(self.promptQuestionBuilder.buildQuestions(promptPairs))
        
        random.shuffle(questions)
        return questions
    
QuestionFactory = QuestionFactory()