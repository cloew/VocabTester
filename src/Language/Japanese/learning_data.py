from .text_converter import TextConverter
from cached_property import cached_property

class LearningData:
    """ Represents the Data specific to Japanese to aid a User in learning that Language """
    
    def __init__(self, language, user):
        """ Intialize with the User """
        self.language = language
        self.user = user
    
    @cached_property
    def textConverter(self):
        """ Return the Text Converter for the User """
        return TextConverter(self.user.learnedSymbolsFor(self.language))