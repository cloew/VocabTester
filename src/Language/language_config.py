
class LanguageConfig:
    """ Represents the Data Configuration for a Language """
    
    def __init__(self, wordDataCls=None):
        """ Initialize the Config with the Word Data Class """
        self.wordDataCls = wordDataCls
        
    @property
    def WordDataCls(self):
        """ Return the Word Data Class """
        return self.wordDataCls if self.wordDataCls else self.doNothing
        
    def doNothing(self, *args, **kwargs):
        return None