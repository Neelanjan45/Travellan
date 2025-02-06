from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_restful import Api

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = r"sqlite:///" + os.path.join(os.getenv("SQLALCHEMY_DATABASE_URI"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

api = Api(app)

import routes
import api_routes

# To autorefresh
# Not for prod
if __name__ == '__main__':
    app.run(debug=True)
