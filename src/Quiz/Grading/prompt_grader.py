from fuzzywuzzy import fuzz

class PromptGrader:
    """ Grades a Prompt Question by checking the entered text is close enough to the answer text """
    
    def grade(self, guess, answer):
        """ Return if the guess matches the answer """
        return fuzz.ratio(guess.lower(), answer) >= 80