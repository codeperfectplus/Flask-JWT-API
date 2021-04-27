from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from waitress import serve

from src.main import app, db

migrate = Migrate(app, db)

if __name__ == '__main__':
    print("Starting server...")
    serve(app, host="0.0.0.0", port=8000)
