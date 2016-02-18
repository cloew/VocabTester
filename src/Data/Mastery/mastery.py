from .staleness_period import StalenessPeriod
from ..symbol_info import SymbolInfo
from ..word_info import WordInfo

from kao_flask.ext.sqlalchemy import db
from datetime import datetime
from sqlalchemy import text, func
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql.expression import cast
import sys

class Mastery(db.Model):
    """ Represents the mastery of some skill """
    __tablename__ = 'masteries'
    MAX_RATING = 5
    CORRECT_CHANGE = 1
    WRONG_CHANGE = -1
    
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")
    
    word_id = db.Column(db.Integer, db.ForeignKey('words.id', ondelete="CASCADE"))
    word = db.relationship("Word")
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbols.id', ondelete="CASCADE"))
    symbol = db.relationship("Symbol")
    
    answerRating = db.Column(db.Integer, server_default=text('0'), nullable=False)
    lastCorrectAnswer = db.Column(db.DateTime)
    
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
        self.updateAnswerDate(correct)
        self.updateRating(correct)
        
        db.session.add(self)
        db.session.commit()
        
    def updateRating(self, correct):
        """ Update the answer rating """
        ratingChange = self.CORRECT_CHANGE if correct else self.WRONG_CHANGE
        
        newRating = self.answerRating + ratingChange
        newRating = min(newRating, self.MAX_RATING)
        newRating = max(newRating, 0)
        self.answerRating = newRating
        
    def updateAnswerDate(self, correct):
        """ Update the answer date """
        if correct:
            self.lastCorrectAnswer = datetime.now()
        
    def updateStalenessPeriod(self, correct):
        """ Update the staleness period based on whether the answer is correct """
        if correct and self.answerRating == self.MAX_RATING and self.isStale:
            self.moveToNextStalenessPeriod()
        elif not correct:
            self.revertToFirstStalenessPeriod()
            
    def moveToNextStalenessPeriod(self):
        """ Move the mastery to the next staleness period """
        self.stalenessPeriod = self.stalenessPeriod.next
        
    def revertToFirstStalenessPeriod(self):
        """ Revert the staleness period to the first staleness period """
        self.stalenessPeriod = StalenessPeriod.getFirstStalenessPeriod()
    
    @property
    def form(self):
        """ Return the Concept Form associated with the Mastery """
        return self.word if self.word_id is not None else self.symbol
    
    @property
    def formInfo(self):
        """ Return the Concept Form Info associated with the Mastery """
        return WordInfo if self.word_id is not None else SymbolInfo
    
    @hybrid_property
    def rating(self):
        """ Return the rating of the mastery """
        return max(0, self.answerRating - self.stalenessRating)
    
    @hybrid_property
    def stalenessRating(self):
        """ Return the staleness rating of the mastery """
        mostRecentCorrectAnswer = self.lastCorrectAnswer
        if mostRecentCorrectAnswer is None:
            return 0
        else:
            return int((datetime.now() - mostRecentCorrectAnswer).days / self.stalenessPeriod.days)
    
    @stalenessRating.expression
    def stalenessRating(self):
        """ Return the Queryable staleness rating of the mastery """
        return func.coalesce(cast(func.extract('epoch', func.now()-self.lastCorrectAnswer)/86400, db.Integer)/StalenessPeriod.days, 0)
            
    def isStale(self):
        """ Return if the mastery is has outlived the staleness period """
        return self.stalenessRating < 0