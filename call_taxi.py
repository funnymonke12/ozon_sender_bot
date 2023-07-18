import json

import requests
import uuid
from config import OAuth


def call_taxi(comm, long, lat, client_long, client_lat, client_phone, fulladdress, client_fulladdress, quantity, product_name):
    myuuid = str(uuid.uuid4())
    url = f'https://b2b.taxi.yandex.net/b2b/cargo/integration/v2/claims/create'
    params = {'request_id': myuuid}
    headers = {'Authorization': f"Bearer {OAuth}",
               'Accept-Language': 'en'}
    body = {
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
    "droppof_point": 2,
    "pickup_point": 1,
    "quantity": quantity,
    "title": product_name,
    "fiscalization": {
        "mark": {
            "code": 'code',
            "kind": 'type_coding'
            }},
    "size": {
        "height": 1000,
        "length": 1000,
        "width": 1000
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
            "phone": client_phone
        },
        "point_id": 1,
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
        "point_id": 2,
        "type": 'source',
        "visit_order": 2

    }
]

    }

    response = requests.post(url, params=params, headers=headers, json=json.dumps(body))
    print(response)
    print(response.text)


    print()
    url = f'https://b2b.taxi.yandex.net/b2b/cargo/integration/v2/claims/create'
    params = {'claim_id': myuuid}
    headers = {'Authorization': f"Bearer {OAuth}",
                'Accept-Language': 'ru'}
    response = requests.get(url, params=params, headers=headers)
    print(response)
    print(response.text)




