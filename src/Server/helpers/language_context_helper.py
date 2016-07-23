from Data import Language, LanguageContext, LearningContext

def BuildLanguageContext(languageId, user):
    """ Return the Language Context for the given Language Id and the User's Native Language """
    foreignLanguage = Language(id=languageId)
    nativeLanguage = Language(id=user.native_language_id)
    return LanguageContext(foreign=foreignLanguage, native=nativeLanguage)

def BuildLearningContext(languageId, user):
    """ Return the Learning Context for the given Language Id and the User's Native Language """
    foreignLanguage = Language.query.get(languageId)
    return LearningContext(user, foreignLanguage)