from .foreign_prompt_question import ForeignPromptQuestion

import random

class PromptQuestionBuilder:
    """ Helper class to construct Prompt Question Builder """
                     
    def buildQuestions(self, pairs):
        """ Build the questions for use in the quiz """
        random.shuffle(pairs)
        return [ForeignPromptQuestion(pair) for pair in pairs]