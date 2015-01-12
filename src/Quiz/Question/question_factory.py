from native_options_question import NativeOptionsQuestion
from translated_options_question import TranslatedOptionsQuestion

from Quiz.ratio_picker import RatioPicker

import random

class WordWithTranslation:

    def __init__(self, native, translation):
        """ Initialize the Word with Translation """
        self.native = native
        self.translation = translation

class QuestionFactory:
    """ Constructs Questions """
    questionClassRatio = RatioPicker([(TranslatedOptionsQuestion, .5),
                                      (NativeOptionsQuestion, .5)])
                     
    def getWords(self, wordList, conceptManager):
        """ Return the Words """
        nativeWords = wordList.getNativeWords(conceptManager)
        translations = wordList.getTranslatedWords(conceptManager)
        words = [WordWithTranslation(native, translation) for native, translation in zip(nativeWords, translations)]
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