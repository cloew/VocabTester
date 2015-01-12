from kao_flask.database import db

from concept import Concept
from language import Language
from native_and_foreign_pair import NativeAndForeignPair

word_list_concepts = db.Table('word_list_concepts', db.Model.metadata,
                              db.Column('word_list_id', db.Integer, db.ForeignKey('word_lists.id')),
                              db.Column('concept_id', db.Integer, db.ForeignKey('concepts.id')))

class WordList(db.Model):
    """ Represents a list of words to quiz """
    __tablename__ = 'word_lists'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode())
    concepts = db.relationship("Concept", secondary=word_list_concepts)
    native_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    nativeLanguage = db.relationship("Language", foreign_keys=[native_id])
    foreign_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    foreignLanguage = db.relationship("Language", foreign_keys=[foreign_id])
    
    def getNativeWords(self, conceptManager):
        """ Return the native words in the word list """
        return conceptManager.findConceptMatches(self.concepts, self.nativeLanguage)
        
    def getForeignWords(self, conceptManager):
        """ Return the foreign words in the word list """
        return conceptManager.findConceptMatches(self.concepts, self.foreignLanguage)
        
    def getWordPairs(self, conceptManager):
        """ Return the word pairs """
        nativeForms = self.getNativeWords(conceptManager)
        foreignForms = self.getForeignWords(conceptManager)
        return [NativeAndForeignPair(native, foreign) for native, foreign in zip(nativeForms, foreignForms)]