
class WordList:
    """ Represents a list of words to quiz """
    
    def __init__(self, name, concepts, nativeLanguage, testLanguage):
        """ Initialize the Word List with the concepts to test and the native and test languages """
        self.name = name
        self.concepts = concepts
        self.nativeLanguage = nativeLanguage
        self.testLanguage = testLanguage
        
    def getNativeWords(self, conceptManager):
        """ Return the native words in the word list """
        return conceptManager.findConceptMatches(concepts, self.nativeLanguage)
        
    def getTranslatedWords(self, conceptManager):
        """ Return the translated words in the word list """
        return conceptManager.findConceptMatches(concepts, self.testLanguage)