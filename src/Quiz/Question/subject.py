from cached_property import cached_property
from proxy_attrs import  proxy_for

@proxy_for('pair', ['native', 'foreign'])
class Subject:
    """ Represents the Subject of a Question """
    
    def __init__(self, pair, nativeOrForeign):
        """ Initialize with the Concept Pair and whether to display the native or Foriegn Form """
        self.pair = pair
        self.nativeOrForeign = nativeOrForeign
        
    @cached_property
    def clarification(self):
        """ Return the clarification for the Question's Prompt """
        return self.prompt.clarification if self.prompt.needsClarification else None
        
    @cached_property
    def prompt(self):
        """ Return the form of the Concept Pair to use for the Question """
        return self.nativeOrForeign(self.pair)
        
    @cached_property
    def answerForm(self):
        """ Return the form of the Concept Pair to use for the Answer """
        return self.nativeOrForeign.other(self.pair)