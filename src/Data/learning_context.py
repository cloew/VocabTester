from .language_context import LanguageContext

class LearningContext:
    """ Represents the Context of a User learning a Language """
    
    def __init__(self, user, foreign):
        """ Initialize with the User and the Foreign Language """
        self.user = user
        self.languageContext = LanguageContext(foreign=foreign, native=user.nativeLanguage)