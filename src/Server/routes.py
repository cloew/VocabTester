from Server.Controller.quiz_answer_controller import QuizAnswerController
from Server.Controller.quiz_controller import QuizController
from Server.Controller.word_lists_controller import WordListsController

from kao_flask.endpoint import Endpoint
from kao_flask.controllers.html_controller import HTMLController

routes = [Endpoint('/', get=HTMLController('Server/templates/index.html')),
          Endpoint('/api/wordlists', get=WordListsController()),
          Endpoint('/api/wordlist/<int:wordlistId>/quiz', get=QuizController()),
          Endpoint('/api/wordlist/<int:wordlistId>/quiz/answer', post=QuizAnswerController())]