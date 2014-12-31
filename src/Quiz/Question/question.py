import random

class CorrectResults:
    """ Represents a correct answer to a question """
    
    def __init__(self, answer):
        """ Initialize the Correct Results with the answer """
        self.answer = answer
        
    def __unicode__(self):
        """ Return the string representation of the results """
        return u"Correct: {0}".format(self.answer)

class IncorrectResults:
    """ Represents an incorrect answer to a question """
    
    def __init__(self, guess, answer):
        """ Initialize the Incorrect Results with the answer """
        self.guess = guess
        self.answer = answer
        
    def __unicode__(self):
        """ Return the string representation of the results """
        return u"Wrong: {0}. Correct answer was {1}".format(self. guess, self.answer)

class Question:
    """ Represents a question in a Quiz """
    NUM_WRONG_ANSWERS = 4
    
    def __init__(self, word, translation, otherOptions):
        """ Initialize the question with the word to display, its matching translation and the other options """
        self.word = word
        self.translation = translation
        self.otherOptions = otherOptions
        
        self.options = [self.translation] + random.sample(self.otherOptions, self.numberOfWrongAnswers)
        random.shuffle(self.options)
        
    def answer(self, answerIndex):
        """ Return the answer results """
        answer = self.options[answerIndex]
        if answer is self.translation:
            return CorrectResults(answer)
        else:
            return IncorrectResults(answer, self.translation)
        
    @property
    def numberOfWrongAnswers(self):
        """ Returns the number of wrong answers for this question """
        return min(len(self.otherOptions), self.NUM_WRONG_ANSWERS)
        
    @property
    def answerIndex(self):
        """ Return the index of the answer to the question """
        return self.options.index(self.translation)