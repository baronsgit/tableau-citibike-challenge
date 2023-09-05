
import requests as req
import json as js
from geopy.geocoders import Nominatim
from citipy import citipy

# def get_city_zip(lat, lon):
#     geolocator = Nominatim(user_agent="http")
#     location = geolocator.reverse(str(lat) + "," + str(lon))
#     address = location.raw['address']
#     city = address.get('city', '')
#     zipcode = address.get('postcode', '')
#     return city, zipcode

def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=4b2c7a0a4c3f0d2f8a1e0d4f5e4b0b5b"
    response = req.get(url)
    data = js.loads(response.text)
    return data

# create a function to get the zip code and city from a give lat/lon using citipy
def get_city_zip(lat, lon):
    city = citipy.nearest_city(lat, lon)
    return city.city_name, city.country_code

# create a function to get the zip code from a give lat/lon using citipy
def get_zip(lat, lon):
    city = citipy.nearest_city(lat, lon)
    return city.country_code

