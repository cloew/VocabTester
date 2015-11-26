from . import urls
from .admin_json_factory import toJson
from .concepts_to_json import ConceptsToJson
from .Controllers import CreateListConcept, DeleteListConcept, GetListConcepts
from ..auth import auth
from ..decorators import requires_admin
from Data import Concept, Language, Symbol, SymbolList, SymbolInfo, User, Word, WordList, WordInfo

from kao_flask import Routes, Endpoint
from kao_flask.ext.sqlalchemy import CrudEndpoints

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
                Endpoint(urls.SymbolListConcepts, get=GetListConcepts(SymbolInfo)),
                Endpoint(urls.SymbolListConcept, post=CreateListConcept(SymbolInfo), delete=DeleteListConcept(SymbolInfo)),
                CrudEndpoints('/api/admin/wordlists', WordList, toJson, decorators=[auth.requires_auth, requires_admin]),
                Endpoint(urls.WordListConcepts, get=GetListConcepts(WordInfo)),
                Endpoint(urls.WordListConcept, post=CreateListConcept(WordInfo), delete=DeleteListConcept(WordInfo)))