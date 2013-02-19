from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://moody:moody@localhost/moody'
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)
  
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

class Event(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text(80))
  at = db.Column(db.DateTime)
  location = db.Column(db.String(255))
  origin_data = db.Column(db.Text)

class Source(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text(80))
  
class Aspect(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text(80))
  

class Organization(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text(80))
   
class Tag(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text(80))
  

