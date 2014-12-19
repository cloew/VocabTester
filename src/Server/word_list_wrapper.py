from word_wrapper import GetWordListJSON

class WordListWrapper:
    """ Converts a Word List to JSON """
    
    def __init__(self, wordList):
        """ Initialize the word list wrapper """
        self.wordList = wordList
        
    def toJSON(self, conceptManager):
        """ Convert the word list to JSON """
        return {"name":self.wordList.name,
                "words":GetWordListJSON(self.wordList.getNativeWords(conceptManager))}