from flask_marshmallow import Marshmallow

from config import app

ma = Marshmallow(app)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'public_id', 'username', 'admin')

class TodoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'todo_name', 'is_complete', 'author')
