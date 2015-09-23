from .concept_list import concept_list_proxy, query_via_concept_list
from .concept_pair_retriever import ConceptPairRetriever
from .symbol import Symbol

from kao_flask.ext.sqlalchemy import db

@query_via_concept_list(isWords=False)
@concept_list_proxy('conceptList')
class SymbolList:
    """ Represents a list of symbols to quiz """
    getConceptPairs = ConceptPairRetriever(Symbol)
    
    def __init__(self, conceptList):
        """ Initialize the Symbol List """
        self.conceptList = conceptList