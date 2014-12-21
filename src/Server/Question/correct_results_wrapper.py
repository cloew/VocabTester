from Server.word_wrapper import WordWrapper

class CorrectResultsWrapper:
    """ Converts Correct Question Results to JSON """
    
    def __init__(self, results):
        """ Initialize the Wrapper with the results """
        self.results = results
        
    def toJSON(self):
        """ Return the JSON for the results """
        return {"correct":True,
                "answer":WordWrapper(self.results.answer).toJSON()}