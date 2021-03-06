from .concept import Concept
from ..language import Language
from ..Ambiguity import AmbiguityGroup
from ..Mastery import Mastery

from kao_flask.ext.sqlalchemy import db
from sqlalchemy.ext.hybrid import hybrid_method

class Symbol(db.Model):
    """ Represents a symbol used in a language """
    __tablename__ = 'symbols'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.UnicodeText())
    concept_id = db.Column(db.Integer, db.ForeignKey('concepts.id', ondelete="CASCADE"))
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id', ondelete="CASCADE"))
    
    ambiguity_group_id = db.Column(db.Integer, db.ForeignKey(AmbiguityGroup.id, ondelete="SET NULL"))
    clarification = db.Column(db.UnicodeText())
    
    concept = db.relationship("Concept")
    language = db.relationship("Language")
    ambiguity_group = db.relationship(AmbiguityGroup, backref="symbols")
    
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
        return self.ambiguity_group_id is not None
        
    def ambiguousWith(self, other):
        """ Return if this Symbol is ambiguous with the other Symbol """
        return self.text == other.text or self.matchingAmbiguityGroup(other)
        
    def matchingAmbiguityGroup(self, other):
        """ Return whether this Symbol matches the other Symbol's Ambiguity Group """
        if self.ambiguity_group_id is not None:
            return self.ambiguity_group_id == other.ambiguity_group_id
        else:
            return False
    
    def __unicode__(self):
        """ Return the string representation of the Word """
        return unicode(self.text)
        
    def __repr__(self):
        """ Return the String representation of the Symbol """
        return "<Symbol({0}, {1})>".format(self.id, self.language.name)