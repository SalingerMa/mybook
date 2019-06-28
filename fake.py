# -*- coding: utf-8 -*-
from flask_script import Shell, Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from app.model.base import db

app = create_app()


manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()