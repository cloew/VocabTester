from question import Question

class ForeignOptionsQuestion(Question):
    """ Represents a question where all the options are in the foreign language """
    
    def getQuestionForm(self, subject):
        """ Return the proper form of the option pair to use """
        return subject.native
    
    def getOptionForm(self, option):
        """ Return the proper form of the option pair to use """
        return option.foreign