# using flask_sqlalchemy to manipulate mysql tables
import pymysql

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()
app = Flask(__name__)

class Config(object):
    # set db connection config paras
    user = 'root'
    password = 'xxxxxxxx'
    database = 'testdb'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@127.0.0.1:3306/%s' % (user, password, database)
    # sqlalchemy auto track modification
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # show mysql grammar when query
    app.config['SQLALCHEMY_ECHO'] = True
    # forbid auto commit changes
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

# app config -> using existed database for operation below...
app.config.from_object(Config)

# sqlalchemy tool obj
db = SQLAlchemy(app)

class User(db.Model):
    # table_name
    __tablename__ = 'user'  
    # column -> db.Integer
    # dict = {'Name':"geek", "Age":234, "Date":x, "programming":"python"}
    Name = db.Column(db.String(64), primary_key=True, autoincrement=False)
    Age = db.Column(db.String(64), unique=False)
    Date = db.Column(db.String(64))
    programming = db.Column(db.String(64))
    def __init__(self, tmpdict):
        self.Name = tmpdict["Name"] 
        self.Age = tmpdict["Age"] 
        self.Date = tmpdict["Date"] 
        self.programming = tmpdict["programming"] 

if __name__ == '__main__':
    # delete all table in db
    db.drop_all()
    # create all table in db
    db.create_all()

