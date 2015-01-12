from question import Question

class NativeOptionsQuestion(Question):
    """ Represents a question where all the options are in the native language """
    
    def __init__(self, word, options):
        """ Initialize the Question """
        options.remove(word)
        Question.__init__(self, word, word.translation, word.native, [option.native for option in options])
        options.add(word)