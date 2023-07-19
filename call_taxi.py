import json
import time

import requests
import uuid
from config import OAuth


def call_taxi(comm, long, lat, client_long, client_lat, client_phone, fulladdress, client_fulladdress, quantity, product_name):
    myuuid = str(uuid.uuid4())
    print(myuuid)
    url = f'https://b2b.taxi.yandex.net/b2b/cargo/integration/v2/claims/create'
    params = {'request_id': myuuid}
    headers = {'Authorization': f"Bearer {OAuth}",
               'Accept-Language': 'en'}
    request_body = {
'comment': comm,
"client_requirements": {
        "taxi_class": 'express'
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
            "fullname": fulladdress
        },
        "contact": {
            "name": 'Ivan',
            "phone": '+79055935860'
        },
        "point_id": 0,
        "type": 'source',
        "visit_order": 1
    },
    {
        "address": {
            "coordinates": [float(client_long), float(client_lat)],
            "fullname": client_fulladdress
        },
        "contact": {
            "name": 'Ivan',
            "phone": client_phone
        },
        "point_id": 1,
        "type": 'destination',
        "visit_order": 2
    }
]

    }

    response = requests.post(url, params=params, headers=headers, json=request_body)
    print(response)
    print(response.text)
    print(type(response.text))
    order_id = json.loads(response.text)['id']
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




