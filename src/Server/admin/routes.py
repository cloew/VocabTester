from ..auth import auth
from ..decorators import requires_admin
from ..helpers.admin_json_factory import toJson
from Data import Concept, Language, Symbol, SymbolList, User, Word, WordList
from Data.Cache import ConceptFormCache

from kao_flask import Routes
from kao_flask.ext.sqlalchemy import CrudEndpoints

def ConceptsToJson(object, **kwargs):
    """ Add a Query Helper and return the Json """
    user = kwargs['user']
    concepts = object if hasattr(object, '__len__') and len(object) > 0 else [object]
    kwargs['symbolCache'] = ConceptFormCache(Symbol, concepts, [user.nativeLanguage])
    kwargs['wordCache'] = ConceptFormCache(Word, concepts, [user.nativeLanguage])
    return toJson(object, **kwargs)

routes = Routes(CrudEndpoints('/api/admin/users', User, toJson,
                        jsonColumnMap={'nativeLanguage': lambda value: ('native_language_id', value['id'])}, 
                        decorators=[auth.requires_auth, requires_admin]),
                CrudEndpoints('/api/admin/languages', Language, toJson, decorators=[auth.requires_auth, requires_admin]),
                CrudEndpoints('/api/admin/concepts', Concept, ConceptsToJson, decorators=[auth.requires_auth, requires_admin]),
                CrudEndpoints('/api/admin/concepts/<int:conceptId>/words', Word, toJson, 
                            routeParams={'conceptId':'concept_id'}, 
                            jsonColumnMap={'language': lambda value: ('language_id', value['id'])}, 
                            decorators=[auth.requires_auth, requires_admin]),
                CrudEndpoints('/api/admin/concepts/<int:conceptId>/symbols', Symbol, toJson, 
                            routeParams={'conceptId':'concept_id'}, 
                            jsonColumnMap={'language': lambda value: ('language_id', value['id'])}, 
                            decorators=[auth.requires_auth, requires_admin]),
                CrudEndpoints('/api/admin/symbollists', SymbolList, toJson, decorators=[auth.requires_auth, requires_admin]),
                CrudEndpoints('/api/admin/wordlists', WordList, toJson, decorators=[auth.requires_auth, requires_admin]))