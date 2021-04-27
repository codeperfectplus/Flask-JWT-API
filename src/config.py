import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app

app = create_app()
