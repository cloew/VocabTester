from .mastery import Mastery
from kao_flask.ext.sqlalchemy import db

import functools

class MasteryRetriever(object):
    """ Helper descriptor to provide method to retrieve the mastery for a user """

    def __init__(self, masteryFieldName):
        """ Initialize the Mastery Retriever with the prefix for the mastery id """
        self.masteryFieldName = masteryFieldName
        
    def __get__(self, obj, objtype=None):
        """ Return this descriptor or the getMastery method """
        if obj is None:
            return self
        return functools.partial(self.getMastery, obj)

    def getMastery(self, obj, user):
        """ Return the object's mastery record for the given user """
        kwargs = {'user_id':user.id, self.masteryFieldName+'_id':obj.id}
        mastery = Mastery.query.filter_by(**kwargs).first()
        if mastery is None:
            kwargs = {'user':user, self.masteryFieldName:obj}
            mastery = Mastery(**kwargs)
            db.session.add(mastery)
            db.session.commit()
        return mastery