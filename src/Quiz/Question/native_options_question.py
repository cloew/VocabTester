from .options_question import OptionsQuestion

class NativeOptionsQuestion(OptionsQuestion):
    """ Represents a question where all the options are in the native language """
    
    def getQuestionForm(self, subject):
        """ Return the proper form of the option pair to use """
        return subject.foreign
    
    def getOptionForm(self, option):
        """ Return the proper form of the option pair to use """
        return option.native