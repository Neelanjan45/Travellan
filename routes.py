from app import app
from flask import render_template
from models import Locations, Sites
from sqlalchemy import inspect

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/locations")
def locations():
    locations = Locations.query.all()
    return render_template('locations.html', locations=locations)

@app.route("/sites")
def sites():
    sites = Sites.query.all()
    return render_template('sites.html', sites=sites)
