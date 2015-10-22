from .symbol import Symbol
from .symbol_list import SymbolList

class SymbolInfo:
    """ Helper class to hold info regarding the Symbol Form """
    formModel = Symbol
    listModel = SymbolList
    masteryFieldName = 'symbol_id'
    learnedField = 'learnedSymbols'