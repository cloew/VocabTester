from .grade_result import GradeResult
from fuzzywuzzy import fuzz

class PromptGrader:
    """ Grades a Prompt Question by checking the entered text is close enough to the answer text """
    CLOSE_ENOUGH_RATIO = 80
    
    def grade(self, guess, answer):
        """ Return if the guess matches the answer """
        ratio = fuzz.ratio(guess.lower(), answer)
        correct = ratio >= self.CLOSE_ENOUGH_RATIO
        imperfect = ratio < 100
        return GradeResult(correct, imperfect=imperfect)