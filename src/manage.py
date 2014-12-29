from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from Server import server

migrate = Migrate(server.app, server.db)
manager = Manager(server.app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()