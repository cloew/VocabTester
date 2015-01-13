from kao_flask.ext.sqlalchemy.database import db

class Concept(db.Model):
    """ Represents a concept """
    __tablename__ = 'concepts'
    
    id = db.Column(db.Integer, primary_key=True)