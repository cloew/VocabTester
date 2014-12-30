from kao_flask.database import db

from concept import Concept
from language import Language

word_list_concepts = db.Table('word_list_concepts', db.Model.metadata,
                              db.Column('word_list_id', db.Integer, db.ForeignKey('word_lists.id')),
                              db.Column('concept_id', db.Integer, db.ForeignKey('concepts.id')))

class WordList:
    """ Represents a list of words to quiz """
    __tablename__ = 'word_lists'
    
    id = db.Column(db.Integer, primary_key=True)
    concepts = db.relationship("Concept", secondary=word_list_concepts)
    native_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    nativeLanguage = db.relationship("Language", foreign_keys=[native_id])
    test_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    testLanguage = db.relationship("Language", foreign_keys=[test_id])
    
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