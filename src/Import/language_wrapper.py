from Data.language import Language
from Server import server

from kao_decorators import lazy_property

class LanguageWrapper:
    """ Wrapper to properly load a Language from a Langauge Egg """
    
    def __init__(self, languageName):
        """ Initialize with the language name """
        self.languageName = languageName
        
    def exists(self):
        """ Return if this language is already in the database """
        return self.existingLanguage is not None
        
    @lazy_property
    def language(self):
        """ Return the language model """
        return self.existingLanguage if self.existingLanguage else self.buildLanguage()
        
    @lazy_property
    def existingLanguage(self):
        """ Return the existing language model object """
        return Language.query.filter_by(name=self.languageName).first()
            
    def buildLanguage(self):
        """ Build the Language """
        language = Language(name=self.languageName)
        server.db.session.add(language)
        return language