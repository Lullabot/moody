# -*- coding: utf-8 -*-
"""
Flask-Login example
===================
This is a small application that provides a trivial demonstration of
Flask-Login, including remember me functionality.

:copyright: (C) 2011 by Matthew Frazier.
:license:   MIT/X11, see LICENSE for more details.

Modified from flask-user-system
https://github.com/Liuchang0812/flask-user-system
"""
from flask import Flask
from flask import request, render_template, redirect, url_for, flash, session, escape
from flask.ext import sqlalchemy
from flask.ext.login import (LoginManager, current_user, login_required,
                            login_user, logout_user, session, UserMixin,
                            AnonymousUser, confirm_login, fresh_login_required)

class User(UserMixin):
    def __init__(self, name, id, active=True):
        self.name = name
        self.id = id
        self.active = active

    def is_active(self):
        return self.active


class Anonymous(AnonymousUser):
    name = u"Anonymous"


USERS = {
    1: User(u"Notch", 1),
    2: User(u"Steve", 2),
    3: User(u"Creeper", 3, False),
}

USER_NAMES = dict((u.name, u) for u in USERS.itervalues())


app = Flask(__name__)

SECRET_KEY = "yeah, not actually a secret"
DEBUG = True

app.config.from_object(__name__)

login_manager = LoginManager()

login_manager.anonymous_user = Anonymous
login_manager.login_view = "login"
login_manager.login_message = u"Please log in to access this page."
login_manager.refresh_view = "reauth"

# check the data
def validate(newuser):
    if len(newone.Password) < 6:
        return 0
    m = re.match('\w+@\w+\.\w+', str(newuser.Email))
    if m is None:
        print 'email is wrong'
        return 0;

    return 1

# @login_manager.user_loader
# def load_user(id):
#     return USERS.get(int(id))


login_manager.setup_app(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/secret")
@fresh_login_required
def secret():
    return render_template("secret.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if 'username' in session:
        flash("You shoult login out first!")
        return redirect(url_for('info'))
    if request.method == 'GET':
        #print "get"
        return render_template('register.html')
    else:
        #print "post"
        username = request.form['username']
        password = request.form['password']
        repassword = request.form['repassword']
        email = request.form['email']

        #print "< %s %s %s>" % (username , password ,email)
        if password != repassword:
            flash("passwords doesn't match!!")
            return render_template('register.html')

        newuser = User(username, email, password)
        #print newuser
        if validate(newuser):
            db.session.add(newuser)
            db.session.commit()
            flash("Registration is successful!")
            session['username'] = newuser.Username
            session['email'] = newuser.Email
            return render_template('index.html',user=newuser)
        else:
            flash("Registration is not successful!")
            return render_template('register.html')
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST" and "username" in request.form:
        username = request.form["username"]
        if username in USER_NAMES:
            remember = request.form.get("remember", "no") == "yes"
            if login_user(USER_NAMES[username], remember=remember):
                flash("Logged in!")
                return redirect(request.args.get("next") or url_for("index"))
            else:
                flash("Sorry, but you could not log in.")
        else:
            flash(u"Invalid username.")
    return render_template("login.html")


@app.route("/reauth", methods=["GET", "POST"])
@login_required
def reauth():
    if request.method == "POST":
        confirm_login()
        flash(u"Reauthenticated.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("reauth.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()
