from mastery_retriever import mastery_retriever

from concept import Concept
from language import Language

from kao_flask.ext.sqlalchemy.database import db

@mastery_retriever('symbol')
class Symbol(db.Model):
    """ Represents a symbol used in a language """
    __tablename__ = 'symbols'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.UnicodeText())
    concept_id = db.Column(db.Integer, db.ForeignKey('concepts.id'))
    concept = db.relationship("Concept")
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    language = db.relationship("Language")
    
    def __unicode__(self):
        """ Return the string representation of the Word """
        return unicode(self.text)