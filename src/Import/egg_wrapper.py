from .language_wrapper import LanguageWrapper
from .forms_wrapper import FormsWrapper

from Data.symbol import Symbol
from Data.word import Word

class EggWrapper:
    """ Helper class to wrap a Language Egg and facilitate its merge into the database """
    
    def __init__(self, egg):
        """ Initialize the wrapper """
        self.egg = egg
        self.language = LanguageWrapper(self.egg.language)
        self.symbolsWrapper = FormsWrapper(self.egg.symbols, Symbol, self.language)
        self.wordsWrapper = FormsWrapper(self.egg.words, Word, self.language)
        
    def loadExisting(self):
        """ Load the existing words and symbols specified in the egg """
        if self.language.exists():
            results = dict(self.wordsWrapper.find())
            return results.items()
        else:
            return []
            
    def load(self, concepts):
        """ Load the egg into the database """
        self.symbolsWrapper.load(concepts)
        self.wordsWrapper.load(concepts)