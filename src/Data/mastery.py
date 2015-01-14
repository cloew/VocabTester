from kao_flask.ext.sqlalchemy.database import db

from user import User
from word import Word

class Mastery(db.Model):
    """ Represents the mastery of some skill """
    __tablename__ = 'masteries'
    MAX_ANSWERS = 3
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    word = db.relationship("Word")
    
    @property
    def numberOfCorrectAnswers(self):
        """ Return the number of correct answers for this word """
        return len([answer for answer in self.answers if answer.correct])