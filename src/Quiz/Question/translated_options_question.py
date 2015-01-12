from question import Question

class TranslatedOptionsQuestion(Question):
    """ Represents a question where all the options are in the translated language """
    
    def __init__(self, word, options):
        """ Initialize the Question """
        options.remove(word)
        Question.__init__(self, word, word.native, word.translation, [option.translation for option in options])
        options.add(word)