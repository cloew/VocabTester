from routes import routes

from kao_flask.server import Server
from kao_flask.ext.sqlalchemy.sqlalchemy_extension import SqlAlchemyExtension

import os

os.environ["DATABASE_URL"]="postgresql://postgres:postgres@localhost/vocab_dev"
os.environ["APP_SETTINGS"]="Server.config.DevelopmentConfig"


server = Server(__name__, config=os.environ["APP_SETTINGS"], routes=routes, extensions=[SqlAlchemyExtension()])