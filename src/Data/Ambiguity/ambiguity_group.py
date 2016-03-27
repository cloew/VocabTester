from kao_flask.ext.sqlalchemy import db

class AmbiguityGroup(db.Model):
    """ Represents a group of words or symbols that are ambiguous with each other """
    __tablename__ = 'ambiguity_groups'
    
    id = db.Column(db.Integer, primary_key=True)