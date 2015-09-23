from .mastery_retriever import MasteryRetriever

from .concept import Concept
from .language import Language

from kao_flask.ext.sqlalchemy import db

class Word(db.Model):
    """ Represents a word from a particular language """
    __tablename__ = 'words'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.UnicodeText())
    concept_id = db.Column(db.Integer, db.ForeignKey('concepts.id'))
    concept = db.relationship("Concept")
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    language = db.relationship("Language")
    
    getMastery = MasteryRetriever('word')
    
    def __unicode__(self):
        """ Return the string representation of the Word """
        return unicode(self.text)