from Server.answer_question_controller import AnswerQuestionController
from Server.next_question_controller import NextQuestionController
from Server.quiz_controller import QuizController
from Server.word_lists_controller import WordListsController

from kao_flask.endpoint import Endpoint
from kao_flask.controllers.html_controller import HTMLController

routes = [Endpoint('/', get=HTMLController('Server/templates/index.html')),
          Endpoint('/api/wordlists', get=WordListsController()),
          Endpoint('/api/wordlist/<int:wordlistId>/quiz', get=QuizController()),
          Endpoint('/api/wordlist/<int:wordlistId>/quiz/answer', post=AnswerQuestionController()),
          Endpoint('/api/wordlist/<int:wordlistId>/quiz/next', post=NextQuestionController())]