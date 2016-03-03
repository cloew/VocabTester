from .concept_list import ConceptList, bound_concept_list
from ..Concept import Symbol

@bound_concept_list(isWords=False)
class SymbolList(ConceptList):
    """ Represents a list of symbols to quiz """
    entry_model = Symbol
        
    def __repr__(self):
        """ Return the string representation """
        return "SymbolList({0})".format(self.name)