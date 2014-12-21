from Quiz.Question.question import CorrectResults, IncorrectResults
from correct_results_wrapper import CorrectResultsWrapper
from incorrect_results_wrapper import IncorrectResultsWrapper

classToWrapperClass = {CorrectResults:CorrectResultsWrapper,
                       IncorrectResults:IncorrectResultsWrapper}

def GetResultsWrapper(results):
    """ Return the proper results wrapper object """
    return classToWrapperClass[results.__class__](results)