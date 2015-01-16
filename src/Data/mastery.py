from kao_flask.ext.sqlalchemy.database import db

from answer import Answer
from user import User

class Mastery(db.Model):
    """ Represents the mastery of some skill """
    __tablename__ = 'masteries'
    MAX_ANSWERS = 3
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    word = db.relationship("Word")
    answers = db.relationship("Answer", order_by=Answer.createdDate, backref=db.backref('mastery'))
    
    def addAnswer(self, correct):
        """ Add an answer to this mastery """
        if len(self.answers) >= self.MAX_ANSWERS:
            db.session.delete(self.answers[0])
        answer = Answer(correct=correct, mastery=self)
        db.session.add(answer)
        db.session.commit()
    
    @property
    def numberOfCorrectAnswers(self):
        """ Return the number of correct answers for this mastery """
        return len([answer for answer in self.answers if answer.correct])
    
    @property
    def rating(self):
        """ Return the rating of the mastery """
        return self.numberOfCorrectAnswers