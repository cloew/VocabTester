from ..language_wrapper import LanguageWrapper

class AmbiguityGroupData:
    """ Represents the data to seed an Ambiguity Group with """
    
    def __init__(self, language, symbols):
        """ Initialize with the Language and Symbols """
        self.language = LanguageWrapper(language)
        self.symbols = symbols