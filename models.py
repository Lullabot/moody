from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://moody:moody@localhost/moody'
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)
  moods = db.relationship('Mood', backref='user', lazy='dynamic')
  events = db.relationship('Event', backref='user', lazy='dynamic')
  tags = db.relationship('Tag', backref='user', lazy='dynamic')
  

  def __init__(self, username, email):
    self.username = username
    self.email = email

  def __repr__(self):
    return '<User %r>' % self.username

class Mood(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  value = db.Column(db.Integer)
  at = db.Column(db.DateTime)
  location = db.Column(db.String(255))
  note = db.Column(db.String(255))
  origin_data = db.Column(db.Text)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __init__(self, value, at, location, note, origin_data, user_id):
    self.value = value
    self.at = at
    self.location = location
    self.note = note
    self.origin_data = origin_data
    self.user_id = user_id
  
  def __repr__(self):
    return '<Mood %r>' % self.value


class Event(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text(80))
  at = db.Column(db.DateTime)
  location = db.Column(db.String(255))
  origin_data = db.Column(db.Text)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __init__(self, name, at, location, origin_data, user_id):
    self.name = name
    self.at = at
    self.location = location
    self.origin_data
    self.user_id = user_id
  
  def __repr__(self):
    return '<Event %r>' % self.name


class Source(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text(80))

  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return '<Source %r>' % self.name


class Aspect(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text(80))

  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return '<Aspect %r>' % self.name


class Organization(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text(80))

  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return '<Organization %r>' % self.name

 
class Tag(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text(80))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  
  def __init__(self, name, user_id):
    self.name = name
    self.user_id = user_id

  def __repr__(self):
    return '<Tag %r>' % self.name


