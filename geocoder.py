import requests
import json

from config import geocoder_key

def get_address(lat, long):
    url = 'https://geocode-maps.yandex.ru/1.x'
    params = {'apikey': geocoder_key,
              'geocode': f'{long}, {lat}',
              'format': 'json'}
    response = requests.get(url, params=params).text
    response = json.loads(response)
    return response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']





