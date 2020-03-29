# https://maps.googleapis.com/maps/api/geocode/json?latlng=15.143479,104.256276&key=AIzaSyCPr8A6Vo8Yjw2q1XCeD8wugso11614GKk

import requests
from pprint import pprint

url = 'https://maps.googleapis.com/maps/api/geocode/json?language=th&latlng=15.143479,104.256276&key=AIzaSyCPr8A6Vo8Yjw2q1XCeD8wugso11614GKk'

response = requests.get(url)
data = response.json()

pprint(data)
