from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

UPLOAD_FOLDER = './app/static/uploads'

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'some$3cretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tfelzzuhxvbbcs:a9f0bc5e6515647d3162d425c5aee205af02f01a2aa3f6efb7ea796a6c15bf89@ec2-52-202-146-43.compute-1.amazonaws.com:5432/dfar6q5fcsnu4a'

# 'postgresql://admin:password@localhost/project1'
db = SQLAlchemy(app)

from app import views, models