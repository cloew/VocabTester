from mastery import Mastery
from kao_flask.ext.sqlalchemy.database import db

def mastery_retriever(masteryFieldName):
    def addMastery(cls):
        def getMastery(self, user):
            """ Return the object's mastery record for the given user """
            kwargs = {'user_id':user.id, masteryFieldName:self.id}
            mastery = Mastery.query.filter_by(**kwargs).first()
            if mastery is None:
                mastery = Mastery(**kwargs)
                db.session.add(mastery)
                db.session.commit()
            return mastery
        
        def getMasteryRating(self, user):
            """ Return the user's mastery rating for this object """ 
            return self.getMastery(user).rating
            
        cls.getMastery = getMastery
        cls.getMasteryRating = getMasteryRating
        return cls
    return addMastery