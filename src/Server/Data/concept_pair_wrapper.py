from Server.Data.word_wrapper import WordWrapper

class ConceptPairWrapper:
    """ Converts a Pair object to JSON """
    
    def __init__(self, pair):
        """ Initialize the pair wrapper """
        self.pair = pair
        
    def toJSON(self, user):
        """ Convert the word list to JSON """
        return {"foreign":WordWrapper(self.pair.foreign).toJSON(user),
                "native":WordWrapper(self.pair.native).toJSON(user)}
        
def GetPairListJSON(conceptPairs, user):
    """ Return a list of pair JSON from the given pairs """
    return [ConceptPairWrapper(conceptPair).toJSON(user) for conceptPair in conceptPairs]