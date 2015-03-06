from question import Question

class NativeOptionsQuestion(Question):
    """ Represents a question where all the options are in the native language """
    
    def getQuestionForm(self, subject):
        """ Return the proper form of the option pair to use """
        return subject.foreign
    
    def getOptionForm(self, option):
        """ Return the proper form of the option pair to use """
        return option.native