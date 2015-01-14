from Data.mastery import Mastery
from Data.user import User

from kao_flask.ext.sqlalchemy.database import db

class UserProxy:
    """ Represents a proxy to lazy load a User object """
    
    def __init__(self, userInfo):
        """ Initialize the proxy with the user info """
        self.userInfo = userInfo
        self.__user = None
        
    @property
    def id(self):
        return self.user.id
        
    @property
    def email(self):
        return self.user.email
        
    @property
    def givenName(self):
        return self.user.givenName
        
    @property
    def lastName(self):
        return self.user.lastName
        
    @property
    def user(self):
        """ Lazy load the user """
        if self.__user is None:
            self.__user = User.query.filter_by(id=self.userInfo[u'id']).first()
        return self.__user
        
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