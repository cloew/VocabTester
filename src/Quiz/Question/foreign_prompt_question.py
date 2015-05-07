
class ForeignPromptQuestion:
    """ Represents a question where the prompt is in the foreign language """
    
    def __init__(self, subject):
        """ Initialize the question with the subject """
        self.subject = subject
        
    @property
    def prompt(self):
        """ Return the text for the prompt """
        return self.subject.foreign.text
        
    @property
    def answer(self):
        """ Return the text for the answer """
        return self.subject.native.text.lower()