from .concept_list import concept_list_proxy, query_via_concept_list

@query_via_concept_list(isWords=True)
@concept_list_proxy('conceptList')
class WordList:
    """ Represents a list of words to quiz """
    
    def __init__(self, conceptList):
        """ Initialize the Word List """
        self.conceptList = conceptList