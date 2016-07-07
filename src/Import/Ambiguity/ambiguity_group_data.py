from ..language_wrapper import LanguageWrapper

from Data import AmbiguityGroup

from cached_property import cached_property

class AmbiguityGroupData:
    """ Represents the data to seed an Ambiguity Group with """
    
    def __init__(self, language, symbols):
        """ Initialize with the Language and Symbols """
        self.language = LanguageWrapper(language)
        self.symbolData = symbols
        for symbolData in self.symbolData:
            symbolData.setLanguage(self.language)
        
    def assign(self):
        """ Assign all of the Symbols in this Group to the proper Ambiguity Group """
        for symbolData in self.symbolData:
            symbolData.assign(self.group)
        
    @cached_property
    def symbols(self):
        """ Return the Symbols for this group """
        return [symbolData.symbol for symbolData in self.symbolData]
        
    @cached_property
    def group(self):
        """ Return the Ambiguity Group for the Symbols """
        ambiguityGroup = None
        for symbol in self.symbols:
            newGroup = symbol.ambiguity_group
            if newGroup != ambiguityGroup:
                if ambiguityGroup is None:
                    ambiguityGroup = newGroup
                else:
                    raise ValueError('These symbols are already split between multiple Ambiguity Groups')
                    
        if ambiguityGroup is None:
            ambiguityGroup = AmbiguityGroup()
        return ambiguityGroup
        
    def __repr__(self):
        """ Return the String Representation of the Group Data """
        return "<AmbiguityGroupData({}, {})>".format(self.language.name, self.symbolData)