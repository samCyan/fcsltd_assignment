
from flask import Blueprint, make_response, jsonify

from investors.models.investors import Investor
from investors.utils import haversine_distance, geolocator

investors_bp = Blueprint('investors', __name__, url_prefix='/investors')


def get_closest_investor(lat, long):
    closest_investor_distance = float("inf")
    closest_investor = None
    for investor in Investor.query.all():
        distance = haversine_distance(
            lat, long, investor.latitude, investor.longitude
        )
        if distance < closest_investor_distance:
            closest_investor_distance = distance
            closest_investor = investor
    return closest_investor


@investors_bp.route("/search/by/location/<location>", methods=["GET"])
def get_closest_investor_by_location(location):
    location = geolocator.geocode(location)
    closest_investor = get_closest_investor(location.latitude, location.longitude)
    return make_response(
        jsonify(
            {
                "closest_investor": {
                    key: getattr(closest_investor, key)
                    for key in ["id", "fullname", "location"]
                }
            }
        )
    )


@investors_bp.route("/search/by/geo-cords/lat/<lat>/long/<long>", methods=["GET"])
def get_closest_investor_by_coordinates(lat, long):
    closest_investor = get_closest_investor(float(lat), float(long))
    return make_response(
        jsonify(
            {
                "closest_investor": {
                    key: getattr(closest_investor, key)
                    for key in ["id", "fullname", "location"]
                }
            }
        )
    )
