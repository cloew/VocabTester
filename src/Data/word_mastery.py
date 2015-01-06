from kao_flask.database import db

from word import Word

class WordMastery(db.Model):
    """ Represents the mastery of a word """
    __tablename__ = 'word_masteries'
    
    id = db.Column(db.Integer, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    word = db.relationship("Word", backref=db.backref('mastery'))