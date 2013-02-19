from models import db

def setup_db():
  db.create_all()
  
if (__name__ == '__main__'):
  setup_db()
