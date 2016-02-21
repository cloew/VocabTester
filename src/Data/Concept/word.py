from .concept import Concept
from ..language import Language
from ..Mastery import Mastery

from kao_flask.ext.sqlalchemy import db
from sqlalchemy.ext.hybrid import hybrid_method

class Word(db.Model):
    """ Represents a word from a particular language """
    __tablename__ = 'words'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.UnicodeText())
    concept_id = db.Column(db.Integer, db.ForeignKey('concepts.id', ondelete="CASCADE"))
    concept = db.relationship("Concept")
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id', ondelete="CASCADE"))
    language = db.relationship("Language")
    
    @hybrid_method
    def ratingFor(self, masteryCache):
        """ Return the rating for the given user """
        return masteryCache[self.id].rating
        # mastery = Mastery.query.filter_by(user_id=user.id, word_id=self.id).first()
        # return mastery.rating if mastery else 0
        
    @ratingFor.expression
    def ratingFor(self, user):
        """ Return the expression to use when querying for a word's rating """
        return Mastery.rating
    
    def __unicode__(self):
        """ Return the string representation of the Word """
        return unicode(self.text)
    
    def __repr__(self):
        """ Return the string representation of the Word """
        return repr(self.text)