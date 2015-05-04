from Data.concept import Concept
from Data.language import Language
from Data.symbol import Symbol
from Data.symbol_list import SymbolList
from Data.word import Word
from Data.word_list import WordList

from Server.helpers.crud_endpoints import CrudEndpoints

from Server.Controller.concept_lists_controller import ConceptListsController
from Server.Controller.current_user_controller import CurrentUserController
from Server.Controller.learned_concepts_controller import LearnedConceptsController
from Server.Controller.login_controller import LoginController
from Server.Controller.quiz_answer_controller import QuizAnswerController
from Server.Controller.quiz_controller import QuizController
from Server.Controller.random_quiz_controller import RandomQuizController
from Server.Controller.register_controller import RegisterController
from Server.Controller.search_controller import SearchController

from kao_flask.endpoint import Endpoint
from kao_flask.controllers.html_controller import HTMLController

routes = [Endpoint('/', get=HTMLController('Server/templates/index.html')),
          # Auth
          Endpoint('/api/login', post=LoginController()),
          Endpoint('/api/register', post=RegisterController()),
          Endpoint('/api/users/current', get=CurrentUserController()),
          # Symbols
          Endpoint('/api/symbols', get=LearnedConceptsController(Symbol)),
          # Symbollists
          Endpoint('/api/symbollists', get=ConceptListsController(SymbolList)),
          Endpoint('/api/symbollist/<int:listId>/quiz', get=QuizController(SymbolList)),
          Endpoint('/api/symbollist/random/quiz', get=RandomQuizController(Symbol)),
          # Words
          Endpoint('/api/words', get=LearnedConceptsController(Word)),
          Endpoint('/api/search', post=SearchController()),
          # Wordlists
          Endpoint('/api/wordlists', get=ConceptListsController(WordList)),
          Endpoint('/api/wordlist/<int:listId>/quiz', get=QuizController(WordList)),
          Endpoint('/api/wordlist/random/quiz', get=RandomQuizController(Word)),
          # Mastery
          Endpoint('/api/mastery/<int:masteryId>/answer', post=QuizAnswerController())]
          
routes += CrudEndpoints('/api/admin/languages', Language).endpoints
routes += CrudEndpoints('/api/admin/concepts', Concept).endpoints
routes += CrudEndpoints('/api/admin/concepts/<int:conceptId>/words', Word, 
                        routeParams={'conceptId':'concept_id'}, 
                        jsonColumnMap={'language': lambda value: ('language_id', value['id'])}).endpoints
routes += CrudEndpoints('/api/admin/concepts/<int:conceptId>/symbols', Symbol, 
                        routeParams={'conceptId':'concept_id'}, 
                        jsonColumnMap={'language': lambda value: ('language_id', value['id'])}).endpoints