from flask_marshmallow import Marshmallow

from src.config import app

ma = Marshmallow(app)

class UserSchema(ma.Schema):
    ''' Schemas to serialize and deserialize the user object '''
    class Meta:
        fields = ('user_id', 'public_id', 'username', 'admin')

class TodoSchema(ma.Schema):
    ''' Schemas to serialize and deserialize the todo object  '''
    class Meta:
        fields = ('todo_id', 'todo_name', 'is_complete', 'author')
