from kao_decorators import proxy_for

@proxy_for('pairs', ['__len__', '__iter__', '__getitem__'])
class UnambiguousGroup:
    """ Represents a group of unambiguous Concept Pairs """
    
    def __init__(self, pair):
        """ Initialize with the starting Concept Pair """
        self.foreignText = set()
        self.nativeText = set()
        self.pairs = []
        
        self._append(pair)
        
    def appendIfUnambiguous(self, pair):
        """ Append the given pair if it is unambiguous with the current contents """
        if self.isUnambiguous(pair):
            self._append(pair)
        
    def _append(self, pair):
        """ Append the pair to the group """
        self.foreignText.add(pair.foreign.text)
        self.nativeText.add(pair.native.text)
        self.pairs.append(pair)
        
    def isUnambiguous(self, other):
        """ Return if the other Concept Pair is unambiguous """
        return self.unambiguousText(other.foreign, self.foreignText) and self.unambiguousText(other.native, self.nativeText)
        
    def unambiguousText(self, otherForm, currentText):
        """ Return if the otherForm's text does not match the text for anything in the Group already """
        return otherForm.text not in currentText