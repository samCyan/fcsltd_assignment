
from geopy.geocoders import Nominatim
from haversine import haversine


geolocator = Nominatim(user_agent="app")

def haversine_distance(lat1, long1, lat2, long2):
    return haversine((lat1, long1), (lat2, long2)) * 1000  # in meters
