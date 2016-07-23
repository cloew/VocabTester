from .language_config import LanguageConfig
from .Japanese import WordData

from enum import Enum
from proxy_attrs import proxy_for

@proxy_for('value', ['WordDataCls'])
class Languages(Enum):
    """ Represents all the Language Configurations available """
    Japanese = LanguageConfig(WordData)
    
    @classmethod
    def forLanguage(cls, language):
        """ Return the Language Config for the given language """
        if language.name in cls.__members__:
            return cls[language.name]
        else:
            return LanguageConfig()