from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from statsbase import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Census(db.Model):
    __tablename__ = 'us'
    __table_args__ = {'schema':'census'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    geocomp = db.Column(db.Text)
    country = db.Column(db.Text)
    region = db.Column(db.Integer)
    division = db.Column(db.Text)
    state = db.Column(db.Text)
    county = db.Column(db.Text)
    countycc = db.Column(db.Text)
    place = db.Column(db.Text)
    pop_count = db.Column(db.Integer)
    housing_unit = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    @property
    def serialize(self):
       return {
           'id': self.id,
           'name': self.name,
           'geocomp': self.geocomp,
           'country': self.country,
           'region': self.region,
           'division': self.division,
           'state': self.state,
           'county': self.county,
           'countycc': self.countycc,
           'place': self.place,
           'population': self.pop_count,
           'housing_unit': self.housing_unit,
           'latitude': self.latitude,
           'longitude': self.longitude,

       }
