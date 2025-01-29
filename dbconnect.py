from app import app

from models import *

with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(f"An error has occured while creating the database schema: {e}")