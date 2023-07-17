import json

import requests
import uuid
from config import OAuth


def call_taxi(comm, long, lat, client_long, client_lat, client_phone, fulladdress, client_fulladdress, quantity, product_name):
    myuuid = uuid.uuid4()
    url = f'https://b2b.taxi.yandex.net/b2b/cargo/integration/v2/claims/create'
    params = {'request_id': myuuid}
    headers = {'Authorization': f"Bearer {OAuth}",
        'Accept-Language': 'ru'}
    body = {
'comment': comm,
"client_requirements": {
        "taxi_class": 'express'
},
"emergency_contact": {
"name": 'Иван',
"phone": 'в описании'
},
"items": [
    {
    "cost_currency": 'RUB',
    "cost_value": '10000',
    "droppof_point": 'int route_points',
    "pickup_point": 'integer (route points.point_id)',
    "quantity": quantity,
    "title": product_name,
    "fiscalization": {
        "mark": {
            "code": 'code',
            "kind": 'type_coding'
            }},
    "size": {
        "height": 'number',
        "length": 'number',
        "width": 'number'
        },

    }],
'route_points': [
    {
        "address": {
            "coordinates": [long, lat],
            "fullname": fulladdress
        },
        "contact": {
            "name": 'Ivan',
            "phone": '88005553535'
        },
        "point_id": 'route_points.id',
        "type": 'source',
        "visit_order": 1

    },
    {
        "address": {
            "coordinates": [client_long, client_lat],
            "fullname": client_fulladdress
        },
        "contact": {
            "name": 'Ivan',
            "phone": client_phone
        },
        "point_id": 'route_points.id',
        "type": 'source',
        "visit_order": 1

    }
]

    }

    response = requests.post(url, params=params, headers=headers, json=body)
    print(response.text)




