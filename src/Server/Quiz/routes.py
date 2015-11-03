from .Controller import AnswerQuestion, GetQuiz, GetRandomQuiz
from Data import SymbolInfo, WordInfo

from kao_flask import Routes, Endpoint

routes = Routes(Endpoint('/api/languages/<int:languageId>/symbollist/<int:listId>/quiz', get=GetQuiz(SymbolInfo)),
                Endpoint('/api/languages/<int:languageId>/symbollist/random/quiz', get=GetRandomQuiz(SymbolInfo)),
                Endpoint('/api/languages/<int:languageId>/wordlist/<int:listId>/quiz', get=GetQuiz(WordInfo)),
                Endpoint('/api/languages/<int:languageId>/wordlist/random/quiz', get=GetRandomQuiz(WordInfo)),
                Endpoint('/api/mastery/<int:masteryId>/answer', post=AnswerQuestion()))