from kao_decorators import lazy_property
from learned_tracker import LearnedTracker

from kao_flask.ext.sqlalchemy.database import db

import random
from hashlib import sha1

learned_symbols = db.Table('learned_symbols', db.Model.metadata,
                                  db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                                  db.Column('symbol_id', db.Integer, db.ForeignKey('symbols.id')))

learned_words = db.Table('learned_words', db.Model.metadata,
                                  db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                                  db.Column('word_id', db.Integer, db.ForeignKey('words.id')))


class User(db.Model):
    """ Represents a user """
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text(), nullable=False, unique=True)
    password = db.Column(db.UnicodeText(), nullable=False)
    givenName = db.Column(db.UnicodeText())
    lastName = db.Column(db.UnicodeText())
    learnedSymbols = db.relationship("Symbol", secondary=learned_symbols)
    learnedWords = db.relationship("Word", secondary=learned_words)
    
    def __init__(self, **kwargs):
        """ Initialize the User """
        if 'password' in kwargs:
            kwargs['password'] = make_password(kwargs['password'])
        db.Model.__init__(self, **kwargs)
        
    def checkPassword(self, rawPassword):
        """ Check if the password is this users password """
        return check_password(rawPassword, self.password)
        
    def tryToLearnSymbol(self, mastery):
        """ Try to learn the symbol related to the given mastery """
        if mastery.symbol_id is not None:
            self.learnedSymbolTracker.tryToLearn(mastery.symbol)
        
    def tryToLearnWord(self, mastery):
        """ Try to learn the word related to the given mastery """
        if mastery.word_id is not None:
            self.learnedWordTracker.tryToLearn(mastery.word)
        
    def save(self):
        """ Save the Underlying User Data Object """
        db.session.add(self)
        db.session.commit()
        
    @lazy_property
    def learnedSymbolTracker(self):
        """ Return the learned tracker for this user's symbols """
        return LearnedTracker(self, 'learnedSymbols', User)
        
    @lazy_property
    def learnedWordTracker(self):
        """ Return the learned tracker for this user's words """
        return LearnedTracker(self, 'learnedWords', User)
    
# borrowing these methods, slightly modified, from flask-peewee which in turn borrowed from django.contrib.auth
def get_hexdigest(salt, raw_password):
    data = salt + raw_password
    return sha1(data.encode('utf8')).hexdigest()

def make_password(raw_password):
    salt = get_hexdigest(unicode(random.random()), unicode(random.random()))[:5]
    hsh = get_hexdigest(salt, raw_password)
    return '%s$%s' % (salt, hsh)

def check_password(raw_password, enc_password):
    salt, hsh = enc_password.split('$', 1)
    return hsh == get_hexdigest(salt, raw_password)