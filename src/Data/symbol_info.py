from .symbol import Symbol
from .symbol_list import SymbolList
from .learned_tables import learned_symbols

class SymbolInfo:
    """ Helper class to hold info regarding the Symbol Form """
    formModel = Symbol
    listModel = SymbolList
    masteryFieldName = 'symbol_id'
    learnedField = 'learnedSymbols'
    learnedTable = learned_symbols