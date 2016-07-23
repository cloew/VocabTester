from Language import Languages

from kao_flask.ext.sqlalchemy import db

from cached_property import cached_property

class Language(db.Model):
    """ Represents a language """
    __tablename__ = 'languages'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    
    @cached_property
    def config(self):
        """ Return the config for this Language """
        return Languages.forLanguage(self)
        
    def __repr__(self):
        """ Return the String Representation of the Language Context """
        return repr(self.name)