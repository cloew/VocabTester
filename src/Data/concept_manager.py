from egg_loader import LoadEgg

class ConceptManager:
    """ Manages connections between words and concepts to allow easy lookup """
    
    def __init__(self, wordEggFilenames):
        """ Initialize the Concept Manager with the concepts and word files to load """
        self.languageToWords = {}
        
        for wordEggFilename in wordEggFilenames:
            language, words = LoadEgg(wordEggFilename)
            self.languageToWords[language] = {word.conceptId:word for word in words}
            
    def findTranslation(self, word, language):
        """ Find the matching translation of the word in the given language """
        conceptToWords = self.languageToWords[language]
        return conceptToWords[word.conceptId]
            
    def findConceptMatches(self, concepts, language):
        """ Return the words matching the given concept ids """
        conceptToWords = self.languageToWords[language]
        return [conceptToWords[conceptId] for conceptId in concepts]