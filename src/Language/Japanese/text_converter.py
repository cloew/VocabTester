from kao_romkan import RomKanConverter

class TextConverter:
    """ Helper class to manage converting Japanese Character strings into a form the User can understand based on their Learned Symbols """
    
    def __init__(self, symbols):
        """ Initialize with the Symbols the User has learned """
        self.converter = RomKanConverter(symbol.text for symbol in symbols)
        
    def convertWord(self, word):
        """ Convert the given Word """
        return self.converter.convert(word.text, readings=word.language_data['readings'])
        
    def convert(self, text, readings={}):
        """ Convert the given text """
        return self.converter.convert(text, readings=readings)
        