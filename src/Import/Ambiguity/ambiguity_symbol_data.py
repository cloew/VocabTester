from cached_property import cached_property

class AmbiguitySymbolData:
    """ Represents the data for a Symbol's Ambiguity """
    
    def __init__(self, text, clarification):
        """ Initialize with the text for the symbol and the Clarification for its Ambiguity group """
        self.text = text
        self.clarification = clarification
    
    @cached_property
    def symbol(self):
        """ Return the Symbol this Data belongs to """
        symbol = Symbol.query.filter_by(text=text, language=self.language.language).first()
        if symbol is None:
            raise ValueError('Unknown symbol {}').format(text)
        return symbol