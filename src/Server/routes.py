from .helpers.admin_json_factory import toJson

from Data import Concept, Language, Symbol, SymbolInfo, User, Word, WordInfo

from .admin.routes import routes as AdminRoutes
from .auth.routes import routes as AuthRoutes
from .Controller import ConceptListsController, LearnedConceptsController
from .Search.routes import routes as SearchRoutes
from .Quiz.routes import routes as QuizRoutes

from kao_flask.endpoint import Endpoint
from kao_flask.controllers.html_controller import HTMLController
from kao_flask.ext.sqlalchemy import ListController

routes = [Endpoint('/', get=HTMLController('Server/templates/index.html')),
          AuthRoutes,
          AdminRoutes,
          # Languages
          Endpoint('/api/languages', get=ListController(Language, toJson)),
          # Symbols
          Endpoint('/api/languages/<int:languageId>/symbols', get=LearnedConceptsController(SymbolInfo)),
          # Symbollists
          Endpoint('/api/languages/<int:languageId>/symbollists', get=ConceptListsController(SymbolInfo)),
          # Words
          Endpoint('/api/languages/<int:languageId>/words', get=LearnedConceptsController(WordInfo)),
          # Wordlists
          Endpoint('/api/languages/<int:languageId>/wordlists', get=ConceptListsController(WordInfo)),
          SearchRoutes,
          QuizRoutes]