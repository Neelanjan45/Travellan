from app import api
from api import LocationsApi

api.add_resource(LocationsApi, '/api/locations')
