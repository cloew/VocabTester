from Data.symbol import Symbol
from Data.symbol_list import SymbolList
from Data.word import Word
from Data.word_list import WordList

from Server.Controller.concept_lists_controller import ConceptListsController
from Server.Controller.current_user_controller import CurrentUserController
from Server.Controller.learned_concepts_controller import LearnedConceptsController
from Server.Controller.login_controller import LoginController
from Server.Controller.quiz_answer_controller import QuizAnswerController
from Server.Controller.quiz_controller import QuizController
from Server.Controller.register_controller import RegisterController

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
          # Words
          Endpoint('/api/words', get=LearnedConceptsController(Word)),
          # Wordlists
          Endpoint('/api/wordlists', get=ConceptListsController(WordList)),
          Endpoint('/api/wordlist/<int:listId>/quiz', get=QuizController(WordList)),
          # Mastery
          Endpoint('/api/mastery/<int:masteryId>/answer', post=QuizAnswerController())]