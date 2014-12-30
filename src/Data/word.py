from kao_flask.database import db

from concept import Concept
from language import Language

class Word(db.Model):
    """ Represents a word from a particular language """
    __tablename__ = 'words'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    concept_id = db.Column(db.Integer, db.ForeignKey('concepts.id'))
    concept = db.relationship("Concept", backref=db.backref('words'))
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    language = db.relationship("Language", backref=db.backref('languages'))
    
    def __init__(self, concept, text):
        """ Initialize the word with its concept and the text """
        self.concept = concept
        self.text = text
        
    def __unicode__(self):
        """ Return the string representation of the Word """
        return unicode(self.text)