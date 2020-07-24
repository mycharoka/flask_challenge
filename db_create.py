from models import db, User

# create databases and the db tables
db.create_all()

# insert
db.session.add(User('testing', 'testing', 1000))
db.session.add(User('test', 'test', 500))

# commit changes
db.session.commit()
