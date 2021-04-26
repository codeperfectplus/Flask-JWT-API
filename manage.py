from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from src.main import app, db

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()