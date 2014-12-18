
class WordListWrapper:
    """ Converts a Word List Wrapper to JSON """
    
    def __init__(self, wordList):
        """ Initialize the word list wrapper """
        self.wordList = wordList
        
    def toJSON(self, conceptManager):
        """ Convert the word list to JSON """
        return {"name":self.wordList.name,
                "words":[unicode(word) for word in self.wordList.getNativeWords(conceptManager)]}