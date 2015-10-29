from .answer import Answer
from .staleness_period import StalenessPeriod
from ..symbol_info import SymbolInfo
from ..word_info import WordInfo

from kao_flask.ext.sqlalchemy import db
import datetime

class Mastery(db.Model):
    """ Represents the mastery of some skill """
    __tablename__ = 'masteries'
    MAX_ANSWERS = 5
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    word = db.relationship("Word")
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbols.id'))
    symbol = db.relationship("Symbol")
    answers = db.relationship("Answer", order_by=Answer.createdDate, backref=db.backref('mastery'), lazy='subquery')
    staleness_period_id = db.Column(db.Integer, db.ForeignKey('staleness_periods.id'))
    stalenessPeriod = db.relationship("StalenessPeriod", lazy='subquery')
    
    def __init__(self, *args, **kwargs):
        """ Initialize the mastery """
        if 'user' in kwargs and hasattr(kwargs['user'], 'user'):
            kwargs['user'] = kwargs['user'].user
        if 'stalenessPeriod' not in kwargs:
            kwargs['stalenessPeriod'] = StalenessPeriod.getFirstStalenessPeriod()
        db.Model.__init__(self, *args, **kwargs)
    
    def addAnswer(self, correct):
        """ Add an answer to this mastery """
        self.updateStalenessPeriod(correct)
        if len(self.answers) >= self.MAX_ANSWERS:
            db.session.delete(self.answers[0])
        answer = Answer(correct=correct, mastery=self)
        db.session.add(answer)
        db.session.commit()
        
    def updateStalenessPeriod(self, correct):
        """ Update the staleness period based on whether the answer is correct """
        if correct and self.answerRating == self.MAX_ANSWERS and self.isStale:
            self.moveToNextStalenessPeriod()
        else:
            self.revertToFirstStalenessPeriod()
            
    def moveToNextStalenessPeriod(self):
        """ Move the mastery to the next staleness period """
        self.stalenessPeriod = self.stalenessPeriod.next
        db.session.add(self)
        
    def revertToFirstStalenessPeriod(self):
        """ Revert the staleness period to the first staleness period """
        self.stalenessPeriod = StalenessPeriod.getFirstStalenessPeriod()
        db.session.add(self)
    
    @property
    def form(self):
        """ Return the Concept Form associated with the Mastery """
        return self.word if self.word_id is not None else self.symbol
    
    @property
    def formInfo(self):
        """ Return the Concept Form Info associated with the Mastery """
        return WordInfo if self.word_id is not None else SymbolInfo
    
    @property
    def numberOfCorrectAnswers(self):
        """ Return the number of correct answers for this mastery """
        return len([answer for answer in self.answers if answer.correct])
    
    @property
    def rating(self):
        """ Return the rating of the mastery """
        return max(0, self.answerRating + self.stalenessRating)
    
    @property
    def answerRating(self):
        """ Return the answer rating of the mastery """
        return self.numberOfCorrectAnswers
    
    @property
    def stalenessRating(self):
        """ Return the staleness rating of the mastery """
        mostRecentCorrectAnswer = self.mostRecentCorrectAnswer
        if mostRecentCorrectAnswer is None:
            return 0
        else:
            return -1 * int((datetime.datetime.now() - mostRecentCorrectAnswer).days / self.stalenessPeriod.days)
    
    @property
    def mostRecentCorrectAnswer(self):
        """ Return the most recent correct answer """
        correctAnswerDates = [answer.createdDate for answer in self.answers if answer.correct]
        if len(correctAnswerDates) == 0:
            return None
        else:
            return max(correctAnswerDates)
            
    @property
    def isStale(self):
        """ Return if the mastery is has outlived the staleness period """
        return self.stalenessRating < 0