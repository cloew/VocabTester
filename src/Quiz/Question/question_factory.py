from translated_options_question import TranslatedOptionsQuestion
import random

class WordCorrelation:

    def __init__(self, native, translation):
        """ Initialize the Word Correlation """
        self.native = native
        self.translation = translation

class QuestionFactory:
    """ Constructs Questions """
    
    def buildQuestions(self, wordList, conceptManager):
        """ Build the questions for use in the quiz """
        nativeWords = wordList.getNativeWords(conceptManager)
        translations = wordList.getTranslatedWords(conceptManager)
        words = [WordCorrelation(native, translation) for native, translation in zip(nativeWords, translations)]
        random.shuffle(words)
        
        setOfWords = set(words)
        return [TranslatedOptionsQuestion(word, setOfWords) for word in words]
        
QuestionFactory = QuestionFactory()