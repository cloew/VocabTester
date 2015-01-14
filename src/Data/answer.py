from kao_flask.ext.sqlalchemy.database import db

from mastery import Mastery

from datetime import datetime

class Answer(db.Model):
    """ Represents an answer for a skill """
    __tablename__ = 'answers'
    
    id = db.Column(db.Integer, primary_key=True)
    correct = db.Column(db.Boolean)
    createdDate = db.Column(db.DateTime, default=datetime.now)
    mastery_id = db.Column(db.Integer, db.ForeignKey('masteries.id'))
    mastery = db.relationship("Mastery", backref=db.backref('answers', order_by=createdDate))
    
    def __repr__(self):
        """ Return the String Representation """
        return "<Answer: {0}:{1}>".format(self.correct, self.createdDate)