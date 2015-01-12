from question import Question

class ForeignOptionsQuestion(Question):
    """ Represents a question where all the options are in the foreign language """
    
    def __init__(self, word, options):
        """ Initialize the Question """
        options.remove(word)
        Question.__init__(self, word, word.native, word.foreign, [option.foreign for option in options])
        options.add(word)