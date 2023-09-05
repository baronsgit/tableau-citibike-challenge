
import requests as req
import json as js
from geopy.geocoders import Nominatim
from citipy import citipy
from pathlib import Path

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

def get_cityzip(lat, lon):
    # get the city and zip code from a given lat, lon using AppZipCode
    city, zip = ZipCodeDB.get_city_zip(lat, lon)
    # # if the city and zip code are not found using AppZipCode, use citipy to get the city and zip code
    # if city == None or zip == None:
    #     city, zip = get_city_zip(lat, lon)

    return city, zip


class ZipCodeDB:
    def __init__(self):
        pass
    # def __init__(self, state):
    #     self.state = state
    #     # self.zipCodeDBData = self._load_zip_code_database(self, state)

    def getStateName(self, state):
        return state
    
    #zipCodeDBData = []

    # # load zip_code_database.csv based on state
    # def _load_zip_code_database(val):
    #     zipDB = []
    #     with open(Path('Resources/zip_code_database.csv')) as f:
    #         for line in f:
    #             if line.strip().split(',')[2] == val:
    #                 zipDB.append(line.strip().split(','))
    #     return zipDB
    
    # # get the city and zip code from a given lat/lon using zipCodeDBData
    # def get_city_zip(self, lat, lon):
    #     for zipCode in self.zipCodeDBData:
    #         if zipCode[3] == lat and zipCode[4] == lon:
    #             return zipCode[1], zipCode[0]
    #     return None, None




# # create a class to hold the zip_code_database.csv data
# class AppZipCode:
#     def __init__(self, zip, city, state, lat, lon):
#         self.zip = zip
#         self.city = city
#         self.state = state
#         self.lat = lat
#         self.lon = lon

#     # # load zip_code_database.csv data in constructor
#     # zip_code_database = []
#     # with open('zip_code_database.csv') as f:
#     #     for line in f:
#     #         zip_code_database.append(AppZipCode(*line.strip().split(',')))

#     # create a function to load the zip_code_database.csv data into a list of ZipCode objects
#     def load_zip_code_database():
#         zip_code_database = []
#         with open('zip_code_database.csv') as f:
#             for line in f:
#                 zip_code_database.append(AppZipCode(*line.strip().split(',')))
#         return zip_code_database
    
#     # create a function to get the city and zip code from a given lat/lon using the zip_code_database.csv data
#     def get_city_zip(lat, lon):
#         zip_code_database = AppZipCode.load_zip_code_database()
#         for zip_code in zip_code_database:
#             if zip_code.lat == lat and zip_code.lon == lon:
#                 return zip_code.city, zip_code.zip
#         return None, None
    
