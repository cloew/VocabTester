from .admin_json_factory import toJson
from Data import Symbol, Word
from Data.Cache import ConceptFormCache

def ConceptsToJson(object, **kwargs):
    """ Add a Query Helper and return the Json """
    user = kwargs['user']
    concepts = object if hasattr(object, '__len__') and len(object) > 0 else [object]
    kwargs['symbolCache'] = ConceptFormCache(Symbol, concepts, [user.nativeLanguage])
    kwargs['wordCache'] = ConceptFormCache(Word, concepts, [user.nativeLanguage])
    return toJson(object, **kwargs)