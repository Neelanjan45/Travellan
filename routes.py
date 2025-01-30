from app import app
from flask import render_template
from models import Locations, Sites

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/locations")
def locations():
    locations = Locations.query.all()
    return render_template('locations.html', locations=locations)
