from egg_loader import LoadEgg

from concept import Concept
from word import Word

class ConceptManager:
    """ Manages connections between words and concepts to allow easy lookup """
    
    def __init__(self, wordEggFilenames):
        """ Initialize the Concept Manager with the concepts and word files to load """
        # self.languageToWords = {}
        
        # for wordEggFilename in wordEggFilenames:
            # language, words = LoadEgg(wordEggFilename)
            # self.languageToWords[language] = {word.conceptId:word for word in words}
            
    def findTranslation(self, word, language):
        """ Find the matching translation of the word in the given language """
        return Word.query.filter_by(concept_id=word.concept_id, language_id=language.id).first()
        # conceptToWords = self.languageToWords[language]
        # return conceptToWords[word.conceptId]
            
    def findConceptMatches(self, conceptIds, language):
        """ Return the words matching the given concept ids """
        with open("temp", 'w') as f:
            f.write(language.name)
        return Word.query.filter_by(language_id=language.id).all()
        return Word.query.filter(Word.concept_id.in_(conceptIds), Word.language_id == language.id).all()
        # conceptToWords = self.languageToWords[language]
        # return [conceptToWords[conceptId] for conceptId in concepts]