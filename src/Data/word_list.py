from .concept_list import concept_list_proxy, query_via_concept_list
from .concept_pair_retriever import ConceptPairRetriever
from .word import Word

from kao_flask.ext.sqlalchemy import db

@query_via_concept_list(isWords=True)
@concept_list_proxy('conceptList')
class WordList:
    """ Represents a list of words to quiz """
    getConceptPairs = ConceptPairRetriever(Word)
    
    def __init__(self, conceptList):
        """ Initialize the Word List """
        self.conceptList = conceptList