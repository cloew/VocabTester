from native_options_question import NativeOptionsQuestion
from foreign_options_question import ForeignOptionsQuestion

from Data.native_and_foreign_pair import NativeAndForeignPair
from Quiz.ratio_picker import RatioPicker

import random

class QuestionFactory:
    """ Constructs Questions """
    questionClassRatio = RatioPicker([(ForeignOptionsQuestion, .5),
                                      (NativeOptionsQuestion, .5)])
                     
    def getWords(self, wordList, conceptManager):
        """ Return the Words """
        nativeForms = wordList.getNativeWords(conceptManager)
        foreignForms = wordList.getForeignWords(conceptManager)
        words = [NativeAndForeignPair(native, foreign) for native, foreign in zip(nativeForms, foreignForms)]
        random.shuffle(words)
        return words
    
    def getQuestionClasses(self, words):
        """ Return the question classes """
        questionClasses = self.questionClassRatio.getResults(len(words))
        random.shuffle(questionClasses)
        return questionClasses
    
    def buildQuestions(self, wordList, conceptManager):
        """ Build the questions for use in the quiz """
        words = self.getWords(wordList, conceptManager)
        questionClasses = self.getQuestionClasses(words)
        
        setOfWords = set(words)
        return [questionClass(word, setOfWords) for word, questionClass in zip(words, questionClasses)]
        
QuestionFactory = QuestionFactory()