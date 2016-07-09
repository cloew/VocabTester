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
    def prompt(self):
        """ Return the text for the Question's Prompt """
        return self.form.text
        
    @cached_property
    def clarification(self):
        """ Return the clarification for the Question's Prompt """
        return self.form.clarification if self.form.needsClarification else None
        
    @cached_property
    def form(self):
        """ Return the form of the Concept Pair to use for the Question """
        return self.nativeOrForeign(self.pair)