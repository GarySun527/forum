#encoding: utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from forum import app
from exts import db
from models import User, Question

manager = Manager(app)

#using Migrate is to set up app and db
migrate = Migrate(app, db)

# manager.py /init/migrate/upgrade
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
