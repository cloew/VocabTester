
class WordWrapper:
    """ Converts words to JSON """
    
    def __init__(self, word):
        """ Initialize the word wrapper """
        self.word = word
        
    def toJSON(self):
        """ Convert the word list to JSON """
        mastery = self.word.mastery
        masteryRating = 0
        if mastery is not None:
            masteryRating = mastery.numberOfCorrectAnswers
            
        return {"id":self.word.id,
                "text":unicode(self.word),
                "mastery":masteryRating}
        
def GetWordListJSON(words):
    """ Return a list of word JSON from the given words """
    return [WordWrapper(word).toJSON() for word in words]