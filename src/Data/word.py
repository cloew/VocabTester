from kao_flask.database import db

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
    
    def answer(self):
        """ Answer the word to add mastery """
        from word_mastery import WordMastery
        from word_answer import WordAnswer
        if self.mastery is None:
            self.mastery = WordMastery(word=self)
            
    def getMastery(self):
        
    def __unicode__(self):
        """ Return the string representation of the Word """
        return unicode(self.text)