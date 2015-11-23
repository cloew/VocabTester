from .concept_list import ConceptList, bound_concept_list

@bound_concept_list(isWords=True)
class WordList(ConceptList):
    """ Represents a list of words to quiz """
        
    def __repr__(self):
        """ Return the string representation """
        return "WordList({0})".format(self.name)