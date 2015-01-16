from Data.language import Language
from Data.mastery import Mastery
from Data.user import User

from kao_flask.ext.sqlalchemy.database import db

class UserProxy:
    """ Represents a proxy to lazy load a User object """
    @classmethod
    def add_property(cls, attr):
        def setter(self, v):
            setattr(self.user, attr, v)
        def getter(self):
            return getattr(self.user, attr)
        setattr(cls, attr, property(getter, setter))
    
    def __init__(self, userInfo):
        """ Initialize the proxy with the user info """
        self.userInfo = userInfo
        self.__user = None
        self.__nativeLanguage = None
        self.__foreignLanguage = None
        
    @property
    def user(self):
        """ Lazy load the user """
        if self.__user is None:
            self.__user = User.query.filter_by(id=self.userInfo[u'id']).first()
        return self.__user
        
    @property
    def nativeLanguage(self):
        """ Return the user's native language """
        if self.__nativeLanguage is None:
            self.__nativeLanguage = Language.query.filter_by(name='English').first()
        return self.__nativeLanguage
        
    @property
    def foreignLanguage(self):
        """ Return the user's foreign language """
        if self.__foreignLanguage is None:
            self.__foreignLanguage = Language.query.filter_by(name='Japanese').first()
        return self.__foreignLanguage
        
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
    
    def __nonzero__(self):
        """ Return if the object is true """
        return self.exists()
        
for attribute in ["id", "email", "givenName", "lastName"]:
    UserProxy.add_property(attribute)