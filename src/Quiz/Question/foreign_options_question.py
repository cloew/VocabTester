from .options_question import OptionsQuestion
from Data import NativeOrForeign

class ForeignOptionsQuestion(OptionsQuestion):
    """ Represents a question where all the options are in the foreign language """
    
    def __init__(self, subjectPair, allPairs):
        """ Initialize with the subjectPair and all the Pairs for the Quiz """
        super().__init__(subjectPair, allPairs, subjectForm=NativeOrForeign.Native, optionsForm=NativeOrForeign.Foreign)
