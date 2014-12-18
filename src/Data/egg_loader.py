from word import Word

from kao_factory.data_source_factory import DataSourceFactory
from kao_factory.factory import Factory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter
from kao_factory.Source.json_source import JsonSource

word_parameters = [PrimitiveParameter("concept"),
                   PrimitiveParameter("text")]
                   
WordFactory = Factory(Word, word_parameters)

class LanaguageWords:
    def __init__(self, language, words):
        self.language = language
        self.words = words
        
parameters = [PrimitiveParameter("language"), ComplexParameter("words", WordFactory.loadAll)]

def LoadEgg(eggFilename):
    """ Loads the given egg and returns the words """
    languageWords = DataSourceFactory(LanaguageWords, parameters, JsonSource(eggFilename)).loadAll()[0]
    return languageWords.language, languageWords.words