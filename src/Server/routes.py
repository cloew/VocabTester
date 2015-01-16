from Data.symbol_list import SymbolList
from Data.word_list import WordList

from Server.Controller.current_user_controller import CurrentUserController
from Server.Controller.login_controller import LoginController
from Server.Controller.quiz_answer_controller import QuizAnswerController
from Server.Controller.quiz_controller import QuizController
from Server.Controller.register_controller import RegisterController
from Server.Controller.word_lists_controller import WordListsController

from kao_flask.endpoint import Endpoint
from kao_flask.controllers.html_controller import HTMLController

routes = [Endpoint('/', get=HTMLController('Server/templates/index.html')),
          # Auth
          Endpoint('/api/login', post=LoginController()),
          Endpoint('/api/register', post=RegisterController()),
          Endpoint('/api/users/current', get=CurrentUserController()),
          # Wordlists
          Endpoint('/api/wordlists', get=WordListsController()),
          Endpoint('/api/wordlist/<int:listId>/quiz', get=QuizController(WordList)),
          # Mastery
          Endpoint('/api/mastery/<int:masteryId>/answer', post=QuizAnswerController())]