from .unambiguous_group import UnambiguousGroup

class AmbiguityHelper:
    """ Helper class to handle checking if forms are ambiuous """
    
    def __init__(self, pairs):
        """ Initialize with the concept pairs """
        self.pairs = pairs
        
    def getUnambiguousPairs(self, core, count):
        """ Return Pairs that are unambiguous between themselves and the given core pair """
        group = UnambiguousGroup(core)
        
        for pair in self.pairs:
            group.appendIfUnambiguous(pair)
                
            if len(group) == count:
                break
        
        return list(group)
    
    def notAmbiguous(self, form, currentSelections):
        """ Return if the form is not ambiguous with the selected forms thus far """
        return form.text not in currentSelections