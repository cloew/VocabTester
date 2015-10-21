from .mastery_retriever import MasteryRetriever

from .concept import Concept
from .language import Language

from kao_flask.ext.sqlalchemy import db

class Symbol(db.Model):
    """ Represents a symbol used in a language """
    __tablename__ = 'symbols'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.UnicodeText())
    concept_id = db.Column(db.Integer, db.ForeignKey('concepts.id'))
    concept = db.relationship("Concept")
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    language = db.relationship("Language")
    
    getMastery = MasteryRetriever('symbol')
    
    def __unicode__(self):
        """ Return the string representation of the Word """
        return unicode(self.text)
        
    def __repr__(self):
        """ Return the String representation of the Symbol """
        return "<Symbol({0}, {1})>".format(self.text, self.language.name)