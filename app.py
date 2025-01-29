from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "proj-travel-plan"
app.config['SQLALCHEMY_DATABASE_URI'] = r"sqlite:///F:\sqlite-tools-win-x64-3480000\travellan.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)