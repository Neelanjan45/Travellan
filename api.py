from app import db
from flask_restful import Resource, reqparse, fields, marshal_with
from models import Locations

location_args = reqparse.RequestParser()
location_args.add_argument('title', type=str, required=True, help="Title can not be blank")
location_args.add_argument('description', type=str, required=True, help="Description can not be blank")

locationFileds = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
}

class LocationsApi(Resource):
    @marshal_with(locationFileds)
    def get(self):
        locations = Locations.query.all()
        return locations
    
    @marshal_with(locationFileds)
    def post(self):
        args = location_args.parse_args()
        location = Locations(title=args["title"], description=args["description"])
        db.session.add(location)
        db.session.commit()
        return location
    