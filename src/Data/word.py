
class Word:
    """ Represents a word from a particular language """
    
    def __init__(self, conceptId, text):
        """ Initialize the word with its concept id and the text """
        self.conceptId = conceptId
        self.text = text
        
    def __unicode__(self):
        """ Return the string representation of the Word """
        return unicode(self.text)