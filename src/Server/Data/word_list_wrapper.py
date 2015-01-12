from Server.Data.native_and_foreign_pair_wrapper import GetPairListJSON

class WordListWrapper:
    """ Converts a Word List to JSON """
    
    def __init__(self, wordList):
        """ Initialize the word list wrapper """
        self.wordList = wordList
        
    def toJSON(self, conceptManager):
        """ Convert the word list to JSON """
        return {"id":self.wordList.id,
                "name":self.wordList.name,
                "concepts":GetPairListJSON(self.wordList.getWordPairs(conceptManager))}