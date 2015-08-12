from .routes import routes

from kao_flask import Server
from kao_flask.ext.sqlalchemy.sqlalchemy_extension import SqlAlchemyExtension
from kao_flask.ext.sslify.sslify_extension import SslifyExtension

import os

server = Server(__name__, config=os.environ["APP_SETTINGS"], routes=routes, extensions=[SqlAlchemyExtension(), SslifyExtension()])