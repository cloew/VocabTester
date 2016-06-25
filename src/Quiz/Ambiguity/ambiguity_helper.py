
class AmbiguityHelper:
    """ Helper class to handle checking if forms are ambiuous """
    
    def __init__(self, pairs):
        """ Initialize with the concept pairs """
        self.pairs = pairs
        
    def getUnambiguousPairs(self, core, count):
        """ Return Pairs that are unambiguous between themselves and the given core pair """
        options = [core]
        for pair in self.pairs:
            for option in options:
                if pair.ambiguousWith(option):
                    break
            else:
                options.append(pair)
                
            if len(options) == count:
                break
        
        return options