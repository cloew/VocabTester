from .concept import Concept
from ..language import Language
from ..Mastery import Mastery

from kao_flask.ext.sqlalchemy import db

from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.hybrid import hybrid_method

class Word(db.Model):
    """ Represents a word from a particular language """
    __tablename__ = 'words'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.UnicodeText())
    language_data = db.Column(JSON)
    concept_id = db.Column(db.Integer, db.ForeignKey('concepts.id', ondelete="CASCADE"))
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id', ondelete="CASCADE"))
    
    concept = db.relationship("Concept")
    language = db.relationship("Language")
    
    @hybrid_method
    def ratingFor(self, masteryCache):
        """ Return the rating for the given user """
        return masteryCache[self.id].rating
        
    @ratingFor.expression
    def ratingFor(self, user):
        """ Return the expression to use when querying for a word's rating """
        return Mastery.rating
        
    @property
    def needsClarification(self):
        """ Return if this Symbol needs Clarification """
        return False
        
    def ambiguousWith(self, other):
        """ Return if this Symbol is ambiguous with the other Symbol """
        return self.text == other.text
    
    def __unicode__(self):
        """ Return the string representation of the Word """
        return unicode(self.text)
    
    def __repr__(self):
        """ Return the string representation of the Word """
        return repr(self.text)