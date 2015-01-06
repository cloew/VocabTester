from kao_flask.database import db

from word import Word

class WordMastery(db.Model):
    """ Represents the mastery of a word """
    __tablename__ = 'word_masteries'
    MAX_ANSWERS = 3
    
    id = db.Column(db.Integer, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    word = db.relationship("Word", backref=db.backref('masteries'))
    
    @property
    def numberOfCorrectAnswers(self):
        """ Return the number of correct answers for this word """
        return len([answer for answer in self.answers if answer.correct])