import requests
import json

from validators import isNumeric
from config import geocoder_key

def get_address(lat, long):
    url = 'https://geocode-maps.yandex.ru/1.x'
    params = {'apikey': geocoder_key,
              'geocode': f'{long}, {lat}',
              'format': 'json'}
    response = requests.get(url, params=params).text
    response = json.loads(response)
    return response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']

def get_coords(address):
    url = 'https://geocode-maps.yandex.ru/1.x'
    params = {'apikey': geocoder_key,
              'geocode': f'{address}',
              'format': 'json'}
    response = requests.get(url, params=params).text
    response = json.loads(response)
    return response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()[::-1]

def define_coords(place):
        if not isNumeric(place.split(', ')[0]):
            lat = get_coords(place)[0]
            long = get_coords(place)[1]
        else:
            lat = place.split(', ')[0]
            long = place.split(', ')[1]
        return lat, long



