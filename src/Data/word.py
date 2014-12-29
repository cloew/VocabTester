from kao_flask.database import db

class Word(db.Model):
    """ Represents a word from a particular language """
    __tablename__ = 'words'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    
    def __init__(self, conceptId, text):
        """ Initialize the word with its concept id and the text """
        self.conceptId = conceptId
        self.text = text
        
    def __unicode__(self):
        """ Return the string representation of the Word """
        return unicode(self.text)