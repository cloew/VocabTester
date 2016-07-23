from .language import Language
from .learn_helper import LearnHelper
from .learned_tables import learned_symbols, learned_words
from .symbol_info import SymbolInfo
from .word_info import WordInfo

from kao_flask.ext.sqlalchemy import db
from cached_property import cached_property

class User(db.Model):
    """ Represents a user """
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text(), nullable=False, unique=True, index=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    givenName = db.Column(db.UnicodeText())
    lastName = db.Column(db.UnicodeText())
    native_language_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    
    nativeLanguage = db.relationship("Language")
    learned_symbols = db.relationship("Symbol", secondary=learned_symbols, lazy='dynamic')
    learned_words = db.relationship("Word", secondary=learned_words, lazy='dynamic')
        
    def getLearnedFor(self, formInfo, language):
        """ Return the learned forms for the given Form Info """
        helper = self.helperFor(formInfo)
        return helper.formsFor(language)
        
    def tryToLearn(self, form, formInfo, learnedCache):
        """ Learn the form unless it has already been learned """
        helper = self.helperFor(formInfo)
        helper.tryToLearn(form, learnedCache)
        
    def save(self):
        """ Save the Underlying User Data Object """
        db.session.add(self)
        db.session.commit()
        
    def helperFor(self, formInfo):
        """ Return the Learn Helper for the given Form Info """
        return self.learnedSymbolsHelper if formInfo is SymbolInfo else self.learnedWordsHelper
        
    def learnedSymbolsFor(self, language):
        """ Return the Learned Symbols for the given Language """
        return self.getLearnedFor(SymbolInfo, language)
        
    @cached_property
    def learnedSymbolsHelper(self):
        """ Helper to manage Learned Symbols """
        return LearnHelper(self, SymbolInfo)
        
    @cached_property
    def learnedWordsHelper(self):
        """ Helper to manage Learned Words """
        return LearnHelper(self, WordInfo)