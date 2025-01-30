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

@app.route("/location/<int:loc_id>")
def location(loc_id):
    location = Locations.query.get(loc_id)
    sites = Sites.query.filter_by(loc_id=loc_id).all()
    return render_template('location.html', location=location, sites=sites)
