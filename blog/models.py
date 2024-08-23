
from datetime import datetime
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
from pytz import utc  # Importing UTC timezone from pytz
from blog import db, login_manager, app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=False, nullable=False)
    lastname = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(20), nullable=False)
    address= db.Column(db.String(20), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

   

    def __repr__(self):
       return f"User('{self.firstname}', '{self.email}', '{self.username}')"
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    date_posted = db.Column(db.DateTime(), nullable=False, default=datetime.now(utc))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

