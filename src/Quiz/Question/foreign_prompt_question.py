from .subject import Subject
from Data import NativeOrForeign

from proxy_attrs import proxy_for

@proxy_for('_subject', ['clarification'])
class ForeignPromptQuestion:
    """ Represents a question where the prompt is in the foreign language """
    
    def __init__(self, subjectPair):
        """ Initialize the question with the subject """
        self._subject = Subject(subjectPair, NativeOrForeign.Foreign)
        
    @property
    def subject(self):
        """ Return the subject Concept Pair """
        return self._subject.pair
        
    @property
    def prompt(self):
        """ Return the text for the prompt """
        return self._subject.prompt
        
    @property
    def answer(self):
        """ Return the text for the answer """
        return self.subject.native.text.lower()
        
    @property
    def displayAnswer(self):
        """ Return the text to display for the answer """
        return self.subject.native.text