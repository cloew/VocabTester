
class WordData:
    """ Represents the Language Specific Word Data for a Japanese Word """
    
    def __init__(self, word):
        """ Initialize with the Language Data """
        self.word = word
        if not word.language_data:
            word.language_data = {}
        self.data = word.language_data
        
    @property
    def readings(self):
        """ Return the readings for the Kanji in the given word """
        self.data.setdefault('readings', {})
        return self.data['readings']
        
    @readings.setter
    def readings(self, value):
        """ Set the Readings Value """
        self.data['readings'] = value

    @readings.deleter
    def readings(self):
        """ Delete the Readings Value """
        del self.data['readings']
        
    def getUserText(self, textConverter):
        """ Return the text the User should see based on the given Text Converter """
        return textConverter.convertWord(self.word)