from routes import routes

from kao_flask.server import Server
from kao_flask.ext.sqlalchemy.sqlalchemy_extension import SqlAlchemyExtension

import os

server = Server(__name__, config=os.environ["APP_SETTINGS"], routes=routes, extensions=[SqlAlchemyExtension()])