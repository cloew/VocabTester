from ..language_wrapper import LanguageWrapper

class AmbiguityGroupData:
    """ Represents the data to seed an Ambiguity Group with """
    
    def __init__(self, language, symbols):
        """ Initialize with the Language and Symbols """
        self.language = LanguageWrapper(language)
        self.symbols = symbols
        
    def __repr__(self):
        """ Return the String Representation of the Group Data """
        return "<AmbiguityGroupData({}, {})>".format(self.language.name, self.symbols)