from routes import routes
from kao_flask.sqlalchemy_server import SqlAlchemyServer
import os

os.environ["DATABASE_URL"]="postgresql://postgres:postgres@localhost/vocab_dev"
os.environ["APP_SETTINGS"]="Server.config.DevelopmentConfig"


server = SqlAlchemyServer(__name__, os.environ["APP_SETTINGS"], routes=routes)