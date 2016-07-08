from Data import Symbol
from cached_property import cached_property

class AmbiguitySymbolData:
    """ Represents the data for a Symbol's Ambiguity """
    
    def __init__(self, text, clarification):
        """ Initialize with the text for the symbol and the Clarification for its Ambiguity group """
        self.text = text
        self.clarification = clarification
        
    def setLanguage(self, language):
        """ Set the Language for this Symbol Data """
        self.language = language
        
    def assign(self, group):
        """ Assign the Symbol's Ambiguity Group and Clarification """
        self.symbol.ambiguity_group = group
        self.symbol.clarification = self.clarification
    
    @cached_property
    def symbol(self):
        """ Return the Symbol this Data belongs to """
        symbol = Symbol.query.filter_by(text=self.text, language=self.language.language).first()
        if symbol is None:
            raise ValueError('Unknown symbol {}'.format(text))
        return symbol
        
    def __repr__(self):
        """ Return the String Representation of the Symbol Data """
        return "<AmbiguitySymbolData({}, {})>".format(self.symbol, self.clarification)
