from .language_context import LanguageContext

from proxy_attrs import proxy_for
from cached_property import cached_property

@proxy_for('languageContext', ['foreign', 'native', 'isForeign', 'isNative'])
class LearningContext:
    """ Represents the Context of a User learning a Language """
    
    def __init__(self, user, foreign):
        """ Initialize with the User and the Foreign Language """
        self.user = user
        self.languageContext = LanguageContext(foreign=foreign, native=user.nativeLanguage)
        
    @cached_property
    def foreignLearningData(self):
        """ Return the Foreign Language's Learning Data """
        return self.foreign.LearningDataCls(self.user)
