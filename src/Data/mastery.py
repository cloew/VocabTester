from kao_flask.ext.sqlalchemy.database import db

from answer import Answer
from staleness_period import StalenessPeriod
from user import User

import datetime

class Mastery(db.Model):
    """ Represents the mastery of some skill """
    __tablename__ = 'masteries'
    MAX_ANSWERS = 3
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    word = db.relationship("Word")
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbols.id'))
    symbol = db.relationship("Symbol")
    answers = db.relationship("Answer", order_by=Answer.createdDate, backref=db.backref('mastery'))
    staleness_period_id = db.Column(db.Integer, db.ForeignKey('staleness_periods.id'))
    stalenessPeriod = db.relationship("StalenessPeriod")
    
    def __init__(self, *args, **kwargs):
        """ Initialize the mastery """
        if 'user' in kwargs and hasattr(kwargs['user'], 'user'):
            kwargs['user'] = kwargs['user'].user
        if 'stalenessPeriod' not in kwargs:
            kwargs['stalenessPeriod'] = StalenessPeriod.query.filter_by(first=True).first()
        db.Model.__init__(self, *args, **kwargs)
    
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
        return max(0, self.answerRating + stalenessRating)
    
    @property
    def answerRating(self):
        """ Return the answer rating of the mastery """
        return self.numberOfCorrectAnswers
    
    @property
    def stalenessRating(self):
        """ Return the staleness rating of the mastery """
        return -1 * int((datetime.datetime.now() - mostRecentCorrectAnswer).days / self.stalenessPeriod.days)
    
    @property
    def mostRecentCorrectAnswer(self):
        """ Return the most recent correct answer """
        return max([answer.createdDate for answer in self.answers if answer.correct])