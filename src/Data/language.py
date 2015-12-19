from kao_flask.ext.sqlalchemy import db

class Language(db.Model):
    """ Represents a language """
    __tablename__ = 'languages'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
        
    def __repr__(self):
        """ Return the String Representation of the Language Context """
        return repr(self.name)