from Server.Data.word_wrapper import WordWrapper

class NativeAndForeignPairWrapper:
    """ Converts a Pair object to JSON """
    
    def __init__(self, pair):
        """ Initialize the pair wrapper """
        self.pair = pair
        
    def toJSON(self):
        """ Convert the word list to JSON """
        return {"foreign":WordWrapper(self.pair.foreign).toJSON(),
                "native":WordWrapper(self.pair.native).toJSON()}
        
def GetPairListJSON(conceptPairs):
    """ Return a list of pair JSON from the given pairs """
    return [NativeAndForeignPairWrapper(conceptPair).toJSON() for conceptPair in conceptPairs]