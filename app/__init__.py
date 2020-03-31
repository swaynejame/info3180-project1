from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

UPLOAD_FOLDER = './app/static/uploads'

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'some$3cretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yjuldvbtozkiqv:e54f8cc0a69ae63191ac8c318f7a84d47fea3ed9f611d16dbbd9f9037cae4c6a@ec2-54-210-128-153.compute-1.amazonaws.com:5432/d7g0a4mcpbfvrj'

# 'postgresql://admin:password@localhost/project1'

db = SQLAlchemy(app)

from app import views, models