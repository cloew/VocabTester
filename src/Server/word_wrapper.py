
class WordWrapper:
    """ Converts words to JSON """
    
    def __init__(self, word):
        """ Initialize the word wrapper """
        self.word = word
        
    def toJSON(self):
        """ Convert the word list to JSON """
        return {"id":self.word.id,
                "text":unicode(self.word)}
        
def GetWordListJSON(words):
    """ Return a list of word JSON from the given words """
    return [WordWrapper(word).toJSON() for word in words]