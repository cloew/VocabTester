from ..language_wrapper import LanguageWrapper

from Data import Symbol

from cached_property import cached_property

class AmbiguityGroupData:
    """ Represents the data to seed an Ambiguity Group with """
    
    def __init__(self, language, symbols):
        """ Initialize with the Language and Symbols """
        self.language = LanguageWrapper(language)
        self.symbolText = symbols
        
    @cached_property
    def symbols(self):
        """ Return the Symbols for this group """
        symbols = []
        for text in self.symbolText:
            symbol = Symbol.query.filter_by(text=text, language=self.language.language).first()
            if symbol is None:
                raise ValueError('Unknown symbol {}').format(text)
            symbols.append(symbol)
        return symbols
        
    def __repr__(self):
        """ Return the String Representation of the Group Data """
        return "<AmbiguityGroupData({}, {})>".format(self.language.name, self.symbolText)