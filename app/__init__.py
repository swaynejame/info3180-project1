from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

UPLOAD_FOLDER = './app/static/uploads'

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'some$3cretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fvshwbumwxfkyf:c1a66a955b43af8f4eb347230569d122e042c74a93db022d3e82da2e8489d672@ec2-18-209-187-54.compute-1.amazonaws.com:5432/d15u2sbqj36mo3'

# 'postgresql://admin:password@localhost/project1'
db = SQLAlchemy(app)

from app import views, models