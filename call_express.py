import time

import requests
import uuid
from config import OAuth


def get_express_price(long, lat, client_long, client_lat, fulladdress, client_fulladdress, taxi_class):
    url = 'https://b2b.taxi.yandex.net/b2b/cargo/integration/v2/check-price'
    headers = {'Authorization': f"Bearer {OAuth}",
               'Accept-Language': 'en'}
    body = {
        'requirements': {'taxi_class': taxi_class},
        'route_points': [
        {
            "coordinates": [float(long), float(lat)],
            "fullname": fulladdress,
        },
        {
            "coordinates": [float(client_long), float(client_lat)],
            "fullname": client_fulladdress,
        }]}
    response = requests.post(url, headers=headers, json=body).json()
    return response["price"]

def call_express(comment_first, comment_second, long, lat, client_long, client_lat, client_phone, fulladdress, client_fulladdress, quantity, product_name, taxi_class):
    myuuid = str(uuid.uuid4())
    url = f'https://b2b.taxi.yandex.net/b2b/cargo/integration/v2/claims/create'
    params = {'request_id': myuuid}
    headers = {'Authorization': f"Bearer {OAuth}",
               'Accept-Language': 'en'}
    request_body = {
"client_requirements": {
        "taxi_class": taxi_class
},
"emergency_contact": {
"name": 'Иван',
"phone": '+79055935860'
},
"items": [
    {
    "cost_currency": 'RUB',
    "cost_value": '10000',
    "droppof_point": 1,
    "pickup_point": 0,
    "quantity": quantity,
    "title": product_name,
    "fiscalization": {
        "mark": {
            "code": 'code',
            "kind": 'type_coding'
            }},
    "size": {
        "height": 20,
        "length": 20,
        "width": 20
        },

    }],
'route_points': [
    {
        "address": {
            "coordinates": [float(long), float(lat)],
            "fullname": fulladdress,
            'comment': comment_first
        },
        "contact": {
            "name": 'Ivan',
            "phone": '+79055935860'
        },
        "point_id": 0,
        "type": 'source',
        "visit_order": 1,
        'skip_confirmation': True
    },

    {
        "address": {
            "coordinates": [float(client_long), float(client_lat)],
            "fullname": client_fulladdress,
            'comment': comment_second
        },
        "contact": {
            "name": 'Ivan',
            "phone": '+79774229344'
        },
        "point_id": 1,
        "type": 'destination',
        "visit_order": 2,
        'skip_confirmation': True
    }
]

    }

    response = requests.post(url, params=params, headers=headers, json=request_body)
    order_id = response.json()['id']
    print(response)
    time.sleep(1)
    confirm_order(order_id)


def confirm_order(order_id):
    url = 'https://b2b.taxi.yandex.net/b2b/cargo/integration/v2/claims/accept'
    params = {'claim_id': order_id}
    headers = {'Authorization': f"Bearer {OAuth}",
               'Accept-Language': 'en',}
    request_body = {'version': 1}
    response = requests.post(url, params=params, headers=headers, json=request_body)
    print(response)
    print(response.text)




