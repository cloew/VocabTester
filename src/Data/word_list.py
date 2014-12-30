from kao_flask.database import db

from language import Language
from word import Word

class WordList:
    """ Represents a list of words to quiz """
    __tablename__ = 'word_lists'
    
    id = db.Column(db.Integer, primary_key=True)
    native_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    nativeLanguage = db.relationship("Language")
    test_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    testLanguage = db.relationship("Language")
    
    def __init__(self, name, concepts, nativeLanguage, testLanguage):
        """ Initialize the Word List with the concepts to test and the native and test languages """
        self.name = name
        self.concepts = concepts
        self.nativeLanguage = nativeLanguage
        self.testLanguage = testLanguage
        
    def getNativeWords(self, conceptManager):
        """ Return the native words in the word list """
        return conceptManager.findConceptMatches(self.concepts, self.nativeLanguage)
        
    def getTranslatedWords(self, conceptManager):
        """ Return the translated words in the word list """
        return conceptManager.findConceptMatches(self.concepts, self.testLanguage)