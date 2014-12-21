from Server.word_wrapper import WordWrapper

class IncorrectResultsWrapper:
    """ Converts Incorrect Question Results to JSON """
    
    def __init__(self, results):
        """ Initialize the Wrapper with the results """
        self.results = results
        
    def toJSON(self):
        """ Return the JSON for the results """
        return {"correct":False,
                "answer":WordWrapper(self.results.answer).toJSON(),
                "guess":WordWrapper(self.results.guess).toJSON()}