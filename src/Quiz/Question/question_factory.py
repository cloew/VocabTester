from native_options_question import NativeOptionsQuestion
from foreign_options_question import ForeignOptionsQuestion

from Quiz.ratio_picker import RatioPicker

import random

class QuestionFactory:
    """ Constructs Questions """
    questionClassRatio = RatioPicker([(ForeignOptionsQuestion, .5),
                                      (NativeOptionsQuestion, .5)])
                     
    def getWords(self, wordList, conceptManager, user):
        """ Return the Words """
        words = wordList.getWordPairs(conceptManager, user)
        random.shuffle(words)
        return words
    
    def getQuestionClasses(self, words):
        """ Return the question classes """
        questionClasses = self.questionClassRatio.getResults(len(words))
        random.shuffle(questionClasses)
        return questionClasses
    
    def buildQuestions(self, wordList, conceptManager, user):
        """ Build the questions for use in the quiz """
        words = self.getWords(wordList, conceptManager, user)
        questionClasses = self.getQuestionClasses(words)
        
        setOfWords = set(words)
        return [questionClass(word, setOfWords) for word, questionClass in zip(words, questionClasses)]
        
QuestionFactory = QuestionFactory()