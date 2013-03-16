# A streamlined mood-tracker for your team.

There are a thousand tools to track your project, all designed to give the team at-a-glance knowledge of your technical status. That's all well and good, but what about the emotional status? Is everyone stressed out? Is one team feeling fiiiiiine while the others are simply fine?

Moody's purpose is to give everyone in a company or organization ultra-simple,
low-friction access to a piece of data: "How are you doin'?" Mood is rated on a
1-5 scale, with 1 being "shitty" and 5 being "spectacular!" Other tools are
great for the details: Yammer, Twitter, Email, bags of flaming crap on the
doorstep, and so on. Moody's reveals the team's aggregate mood so hugs,
conversations, or hi-fives can follow.

##Dependancies

You need a working Flask + SQLAlchemy install

```
bash pip install -f requirements.txt
```

See http://flask.pocoo.org/docs/installation/#installation for instructions on getting set up with virtualenv - after that, you can 'pip install' the following:

* flask
* SQLAlchemy
* Flask-SQLAlchemy
* mysql-python (Watch out for dependencies. I had to get the right version of 'distribute' for python, then install libmysqlclient-dev and python-dev before it would work.)

##Database initialization

To set up the database, check out this repo, set up your environment as described above, then run 'python setupdb.py'.  With any luck, you'll get tables.  Currently, joins are not set up.

