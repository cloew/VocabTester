from .symbol_groups import HIRAGANA_MAP

from cached_property import cached_property
from kao_symbols import convert

class TextConverter:
    """ Helper class to manage converting Japanese Character strings into a form the User can understand based on their Learned Symbols """
    
    def __init__(self, symbols):
        """ Initialize with the Symbols the User has learned """
        self.symbols = {symbol.text for symbol in symbols}
        
    def convert(self, word):
        """ Convert the given Word """
        return convert(word.text, self.symbolMap)
        
    @cached_property
    def symbolMap(self):
        """ Return the map of symbols that should be converted """
        return {key:value for key, value in HIRAGANA_MAP.items() if key not in self.symbols}
        