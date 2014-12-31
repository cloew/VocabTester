from kao_flask.database import db

class Language(db.Model):
    """ Represents a language """
    __tablename__ = 'languages'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    
    # def __init__(self, name):
        # """ Initialize the language with its name """
        # self.name = name