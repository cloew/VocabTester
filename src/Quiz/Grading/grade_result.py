
class GradeResult:
    """ Represents the result from grading a Question """
    
    def __init__(self, correct, imperfect=False):
        """ Initialize with whether the answer is correct """
        self.correct = correct
        self.imperfect = imperfect