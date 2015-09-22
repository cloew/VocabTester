from Data.concept import Concept
from Data.language import Language
from Data.symbol import Symbol
from Data.symbol_list import SymbolList
from Data.user import User
from Data.word import Word
from Data.word_list import WordList

from .auth import auth
from Server.decorators import requires_auth, requires_admin
from Server.helpers.admin_json_factory import toJson

from Server.Controller.concept_lists_controller import ConceptListsController
from Server.Controller.create_user_enrollment import CreateUserEnrollment
from Server.Controller.current_user_controller import CurrentUserController
from Server.Controller.learned_concepts_controller import LearnedConceptsController
from Server.Controller.learn_word_controller import LearnWordController
from Server.Controller.login_controller import LoginController
from Server.Controller.quiz_answer_controller import QuizAnswerController
from Server.Controller.quiz_controller import QuizController
from Server.Controller.random_quiz_controller import RandomQuizController
from Server.Controller.register_controller import RegisterController
from Server.Controller.search_controller import SearchController
from Server.Controller.update_user_controller import UpdateUserController
from Server.Controller.user_enrollments import UserEnrollments

from kao_flask.endpoint import Endpoint
from kao_flask.controllers.html_controller import HTMLController
from kao_flask.ext.sqlalchemy import CrudEndpoints, ListController

routes = [Endpoint('/', get=HTMLController('Server/templates/index.html')),
          # Auth
          Endpoint('/api/login', post=auth.LoginController(toJson)),
          Endpoint('/api/users', post=auth.RegisterController(toJson)),
          Endpoint('/api/users/current', get=auth.CurrentUserController(toJson), put=auth.UpdateUserController(toJson)),
          Endpoint('/api/users/current/enrollments', get=UserEnrollments(), post=CreateUserEnrollment()),
          # Languages
          Endpoint('/api/languages', get=ListController(Language, toJson)),
          # Symbols
          Endpoint('/api/languages/<int:languageId>/symbols', get=LearnedConceptsController(Symbol)),
          # Symbollists
          Endpoint('/api/languages/<int:languageId>/symbollists', get=ConceptListsController(SymbolList)),
          Endpoint('/api/languages/<int:languageId>/symbollist/<int:listId>/quiz', get=QuizController(SymbolList)),
          Endpoint('/api/languages/<int:languageId>/symbollist/random/quiz', get=RandomQuizController(Symbol)),
          # Words
          Endpoint('/api/languages/<int:languageId>/words', get=LearnedConceptsController(Word)),
          Endpoint('/api/words/<int:wordId>/learn', post=LearnWordController()),
          Endpoint('/api/languages/<int:languageId>/search', post=SearchController()),
          # Wordlists
          Endpoint('/api/languages/<int:languageId>/wordlists', get=ConceptListsController(WordList)),
          Endpoint('/api/languages/<int:languageId>/wordlist/<int:listId>/quiz', get=QuizController(WordList)),
          Endpoint('/api/languages/<int:languageId>/wordlist/random/quiz', get=RandomQuizController(Word)),
          # Mastery
          Endpoint('/api/mastery/<int:masteryId>/answer', post=QuizAnswerController())]
          
routes += CrudEndpoints('/api/admin/users', User, toJson, decorators=[requires_auth, requires_admin]).endpoints
routes += CrudEndpoints('/api/admin/languages', Language, toJson, decorators=[requires_auth, requires_admin]).endpoints
routes += CrudEndpoints('/api/admin/concepts', Concept, toJson, decorators=[requires_auth, requires_admin]).endpoints
routes += CrudEndpoints('/api/admin/concepts/<int:conceptId>/words', Word, toJson, 
                        routeParams={'conceptId':'concept_id'}, 
                        jsonColumnMap={'language': lambda value: ('language_id', value['id'])}, 
                        decorators=[requires_auth, requires_admin]).endpoints
routes += CrudEndpoints('/api/admin/concepts/<int:conceptId>/symbols', Symbol, toJson, 
                        routeParams={'conceptId':'concept_id'}, 
                        jsonColumnMap={'language': lambda value: ('language_id', value['id'])}, 
                        decorators=[requires_auth, requires_admin]).endpoints