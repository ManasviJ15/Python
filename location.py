import requests

def get_nearby_location(lat,lng, query = "metro station"):
    api_key = "AIzaSyA1c8osos4cfPashGu2CxPYYeRXw6Vyoh4"
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=2000&type=transit_station&keyword={query}&key={api_key}"
    response = requests.get(url)
    places = response.json()
    return places

lat, lng = 23.1815, 72.6288  # Example coordinates for GIFT City
results = get_nearby_location(lat, lng)
for place in results['results']:
    print(place['name'], place['vicinity'])

from geopy.distance import geodesic
import geopy.geocoders

def get_nearest_poi(lat, lng, query="metro station"):
    geolocator = geopy.geocoders.Nominatim(user_agent="giftcity_bot")
    location = geolocator.reverse((lat, lng))
    return location.address

print(get_nearest_poi(23.1815, 72.6288))
