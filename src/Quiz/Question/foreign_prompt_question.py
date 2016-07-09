from .subject import Subject
from Data import NativeOrForeign

class ForeignPromptQuestion:
    """ Represents a question where the prompt is in the foreign language """
    
    def __init__(self, subjectPair):
        """ Initialize the question with the subject """
        self.subject = Subject(subjectPair, NativeOrForeign.Foreign)
        
    @property
    def answer(self):
        """ Return the text for the answer """
        return self.subject.answerForm.text.lower()
        
    @property
    def displayAnswer(self):
        """ Return the text to display for the answer """
        return self.subject.answerForm.text