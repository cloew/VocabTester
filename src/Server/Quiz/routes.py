from .Controllers import AnswerQuestion, GetQuiz, GetRandomQuiz
from Server.helpers import FormEndpoint

from kao_flask import Routes, Endpoint

routes = Routes(FormEndpoint('/api/languages/<int:languageId>/{formList}/<int:listId>/quiz', get=GetQuiz),
                FormEndpoint('/api/languages/<int:languageId>/{formList}/random/quiz', get=GetRandomQuiz),
                Endpoint('/api/mastery/<int:masteryId>/answer', post=AnswerQuestion()))