from kao_flask.ext.sqlalchemy.database import db

from concept import Concept
from language import Language

class Word(db.Model):
    """ Represents a word from a particular language """
    __tablename__ = 'words'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.UnicodeText())
    concept_id = db.Column(db.Integer, db.ForeignKey('concepts.id'))
    concept = db.relationship("Concept", backref=db.backref('words'))
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    language = db.relationship("Language", backref=db.backref('languages'))
    
    def getMasteryRating(self, user):
        """ Return the user's mastery rating for this word """ 
        mastery = user.getMastery(self)
        masteryRating = 0
        if mastery is not None:
            masteryRating = mastery.numberOfCorrectAnswers
        return masteryRating
    
    def __unicode__(self):
        """ Return the string representation of the Word """
        return unicode(self.text)