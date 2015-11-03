from .helpers.admin_json_factory import toJson

from .admin.routes import routes as AdminRoutes
from .auth.routes import routes as AuthRoutes
from .Concepts.routes import routes as ConceptRoutes
from .Search.routes import routes as SearchRoutes
from .Quiz.routes import routes as QuizRoutes

from Data import Language

from kao_flask.endpoint import Endpoint
from kao_flask.controllers.html_controller import HTMLController
from kao_flask.ext.sqlalchemy import ListController

routes = [Endpoint('/', get=HTMLController('Server/templates/index.html')),
          Endpoint('/api/languages', get=ListController(Language, toJson)),
          AuthRoutes,
          AdminRoutes,
          ConceptRoutes,
          SearchRoutes,
          QuizRoutes]