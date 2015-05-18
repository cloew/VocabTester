from kao_decorators import lazy_property, proxy_for

from Data.language import Language
from Data.mastery import Mastery
from Data.symbol import Symbol
from Data.user import User
from Data.word import Word

from kao_flask.ext.sqlalchemy.database import db

@proxy_for('user', ["id", "email", "givenName", "lastName", "nativeLanguage", "languageEnrollments",
                    "getLearnedSymbolsFor", "hasLearnedSymbol", "tryToLearnSymbol", 
                    "learnedWords", "hasLearnedWord", "tryToLearnWord"])
class UserProxy:
    """ Represents a proxy to lazy load a User object """
    
    def __init__(self, userInfo):
        """ Initialize the proxy with the user info """
        self.userInfo = userInfo
        
    @lazy_property
    def user(self):
        """ Lazy load the user """
        return User.query.filter_by(id=self.userInfo[u'id']).first()
        
    @lazy_property
    def foreignLanguage(self):
        """ Return the user's foreign language """
        return Language.query.filter_by(name='Japanese').first()
        
    def exists(self):
        """ Return if the User record actually exists """
        return self.user is not None
        
    def getMastery(self, word):
        """ Return the User's mastery record of the given word """
        mastery = Mastery.query.filter_by(user_id=self.id, word_id=word.id).first()
        if mastery is None:
            mastery = Mastery(user=self.user, word=word)
            db.session.add(mastery)
            db.session.commit()
        return mastery
        
    def getLearnedFor(self, modelClass, languageId):
        """ Return the learned forms for the given model class """
        if modelClass is Symbol:
            return self.getLearnedSymbolsFor(languageId)
        elif modelClass is Word:
            return self.learnedWords
    
    def __nonzero__(self):
        """ Return if the object is true """
        return self.exists()