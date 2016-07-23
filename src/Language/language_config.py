
class LanguageConfig:
    """ Represents the Data Configuration for a Language """
    
    def __init__(self, learningDataCls=None, wordDataCls=None):
        """ Initialize the Config with the Data Classes """
        self.learningDataCls = learningDataCls
        self.wordDataCls = wordDataCls
        
    @property
    def LearningDataCls(self):
        """ Return the Learning Data Class """
        return self.learningDataCls if self.learningDataCls else self.doNothing
        
    @property
    def WordDataCls(self):
        """ Return the Word Data Class """
        return self.wordDataCls if self.wordDataCls else self.doNothing
        
    def doNothing(self, *args, **kwargs):
        return None