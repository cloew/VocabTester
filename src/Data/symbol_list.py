from .concept_list import concept_list_proxy, query_via_concept_list

@query_via_concept_list(isWords=False)
@concept_list_proxy('conceptList')
class SymbolList:
    """ Represents a list of symbols to quiz """
    
    def __init__(self, conceptList):
        """ Initialize the Symbol List """
        self.conceptList = conceptList