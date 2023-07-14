import requests
import uuid
from config import OAuth


def call_taxi(commentary='Без комментариев'):
    myuuid = uuid.uuid4()
    url = f'https://b2b.taxi.yandex.net/b2b/cargo/integration/v2/claims/create'
    query = {'request_id': myuuid}
    headers = {'Accept-Language': 'ru',
               'Authorization': 'Oauthtoken'}
    params = {"auto_accept": True,
              'comment': commentary}
    response = requests.post(url, params=query, headers=headers, json=params)

    url = f'https://b2b.taxi.yandex.net/b2b/cargo/integration/v2/claims/tracking-links'
    query = {'claim_id': myuuid}
    headers = {'Authorization': 'Oauthtoken'}
    response = requests.post(url, params=query, headers=headers)
    link = response.text["route_points"][0]["sharing_link"]
    return link


