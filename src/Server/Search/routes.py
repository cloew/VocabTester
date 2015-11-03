from .Controllers import LearnWord, Search
from kao_flask import Routes, Endpoint

routes = Routes(Endpoint('/api/words/<int:wordId>/learn', post=LearnWord()),
                Endpoint('/api/languages/<int:languageId>/search', post=Search()))