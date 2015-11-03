from .Controllers import GetConceptLists, GetLearnedConcepts
from Data import SymbolInfo, WordInfo

from kao_flask import Routes, Endpoint

routes = Routes(Endpoint('/api/languages/<int:languageId>/symbols', get=GetLearnedConcepts(SymbolInfo)),
                Endpoint('/api/languages/<int:languageId>/symbollists', get=GetConceptLists(SymbolInfo)),
                Endpoint('/api/languages/<int:languageId>/words', get=GetLearnedConcepts(WordInfo)),
                Endpoint('/api/languages/<int:languageId>/wordlists', get=GetConceptLists(WordInfo)))