from .auth import auth
from .decorators import requires_admin
from .helpers.admin_json_factory import toJson

from Data import Concept, Language, Symbol, SymbolList, User, Word, WordList

from .Controller import ConceptListsController, CreateUserEnrollment, LearnedConceptsController, LearnWordController, SearchController, UserEnrollments
from .Quiz.Controller import AnswerQuestion, GetQuiz, GetRandomQuiz

from kao_flask.endpoint import Endpoint
from kao_flask.controllers.html_controller import HTMLController
from kao_flask.ext.sqlalchemy import CrudEndpoints, ListController, RecordValueProvider

routes = [Endpoint('/', get=HTMLController('Server/templates/index.html')),
          # Auth
          Endpoint('/api/login', post=auth.LoginController(toJson)),
          Endpoint('/api/users', post=auth.RegisterController(toJson, recordValueProvider=RecordValueProvider({'nativeLanguage': lambda value: ('native_language_id', value['id'])}))),
          Endpoint('/api/users/current', get=auth.CurrentUserController(toJson), put=auth.UpdateUserController(toJson, recordValueProvider=RecordValueProvider({'nativeLanguage': lambda value: ('native_language_id', value['id'])}))),
          Endpoint('/api/users/current/enrollments', get=UserEnrollments(), post=CreateUserEnrollment()),
          # Languages
          Endpoint('/api/languages', get=ListController(Language, toJson)),
          # Symbols
          Endpoint('/api/languages/<int:languageId>/symbols', get=LearnedConceptsController(Symbol)),
          # Symbollists
          Endpoint('/api/languages/<int:languageId>/symbollists', get=ConceptListsController(SymbolList)),
          Endpoint('/api/languages/<int:languageId>/symbollist/<int:listId>/quiz', get=GetQuiz(SymbolList)),
          Endpoint('/api/languages/<int:languageId>/symbollist/random/quiz', get=GetRandomQuiz(Symbol)),
          # Words
          Endpoint('/api/languages/<int:languageId>/words', get=LearnedConceptsController(Word)),
          Endpoint('/api/words/<int:wordId>/learn', post=LearnWordController()),
          Endpoint('/api/languages/<int:languageId>/search', post=SearchController()),
          # Wordlists
          Endpoint('/api/languages/<int:languageId>/wordlists', get=ConceptListsController(WordList)),
          Endpoint('/api/languages/<int:languageId>/wordlist/<int:listId>/quiz', get=GetQuiz(WordList)),
          Endpoint('/api/languages/<int:languageId>/wordlist/random/quiz', get=GetRandomQuiz(Word)),
          # Mastery
          Endpoint('/api/mastery/<int:masteryId>/answer', post=AnswerQuestion())]
          
routes += CrudEndpoints('/api/admin/users', User, toJson,
                        jsonColumnMap={'nativeLanguage': lambda value: ('native_language_id', value['id'])}, 
                        decorators=[auth.requires_auth, requires_admin]).endpoints
routes += CrudEndpoints('/api/admin/languages', Language, toJson, decorators=[auth.requires_auth, requires_admin]).endpoints
routes += CrudEndpoints('/api/admin/concepts', Concept, toJson, decorators=[auth.requires_auth, requires_admin]).endpoints
routes += CrudEndpoints('/api/admin/concepts/<int:conceptId>/words', Word, toJson, 
                        routeParams={'conceptId':'concept_id'}, 
                        jsonColumnMap={'language': lambda value: ('language_id', value['id'])}, 
                        decorators=[auth.requires_auth, requires_admin]).endpoints
routes += CrudEndpoints('/api/admin/concepts/<int:conceptId>/symbols', Symbol, toJson, 
                        routeParams={'conceptId':'concept_id'}, 
                        jsonColumnMap={'language': lambda value: ('language_id', value['id'])}, 
                        decorators=[auth.requires_auth, requires_admin]).endpoints