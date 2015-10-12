
class OptionsGrader:
    """ Grades an Option Question by checking the proper option was selected """
    
    def grade(self, guess, answer):
        """ Return if the guess matches the answer """
        return guess == answer