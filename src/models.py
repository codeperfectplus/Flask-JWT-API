from flask_sqlalchemy import SQLAlchemy

from src.config import app

db = SQLAlchemy(app)
class UserModel(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    def __init__(self, public_id, username, password, admin):
        self.public_id = public_id
        self.username = username
        self.password = password
        self.admin = admin

    def __repr__(self):
        return self.username

class TodoModel(db.Model):

    __tablename__ = 'todos'

    todo_id = db.Column(db.Integer, primary_key=True)
    todo_name = db.Column(db.String(100), nullable=False)
    is_complete = db.Column(db.Boolean, nullable=False)
    author = db.Column(db.String(50))

    def __init__(self, todo_name, is_complete, author):
        self.todo_name = todo_name
        self.is_complete = is_complete
        self.author = author

    def __repr__(self):
        return self.todo_name