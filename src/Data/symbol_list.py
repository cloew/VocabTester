from concept_list import concept_list_proxy, query_via_concept_list, concept_pair_retriever
from symbol import Symbol

from kao_flask.ext.sqlalchemy.database import db

@query_via_concept_list(isWords=False)
@concept_list_proxy('conceptList')
@concept_pair_retriever(Symbol)
class SymbolList:
    """ Represents a list of symbols to quiz """
    
    def __init__(self, conceptList):
        """ Initialize the Symbol List """
        self.conceptList = conceptList