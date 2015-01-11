from kao_flask.database import db

from word_mastery import WordMastery

from datetime import datetime

class WordAnswer(db.Model):
    """ Represents an answer for a word """
    __tablename__ = 'word_answers'
    
    id = db.Column(db.Integer, primary_key=True)
    correct = db.Column(db.Boolean)
    createdDate = db.Column(db.DateTime, default=datetime.now)
    word_mastery_id = db.Column(db.Integer, db.ForeignKey('word_masteries.id'))
    word_mastery = db.relationship("WordMastery", backref=db.backref('answers', order_by=createdDate))
    
    def __repr__(self):
        """ Return the String Representation """
        return "<Answer: {0}:{1}>".format(self.correct, self.createdDate)