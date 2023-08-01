import time
from datetime import datetime
import requests
import uuid
from config import OAuth


def get_during_day_price(long, lat, client_long, client_lat, fulladdress, client_fulladdress, taxi_class):
    url = 'https://b2b.taxi.yandex.net/b2b/cargo/integration/v2/check-price'
    headers = {'Authorization': f"Bearer {OAuth}",
               'Accept-Language': 'en'}
    hour = datetime.now().hour
    body = {
        'requirements': {
            'taxi_class': taxi_class,
            'same_day_data': {
                'delivery_interval': {
                    'from': datetime.now().strftime(f"%Y-%m-%dT{hour-2}:%M:%SZ"),
                    'to': datetime.now().strftime(f"%Y-%m-%dT{hour-2+4}:%M:%SZ")
            }
            }
        },
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
    print(response)
    return response["price"]


def call_during_day(comment_first, comment_second, long, lat, client_long, client_lat, client_phone, fulladdress, client_fulladdress, quantity, product_name, date_start, date_end):
    myuuid = str(uuid.uuid4())
    url = f'https://b2b.taxi.yandex.net/b2b/cargo/integration/v2/claims/create'
    params = {'request_id': myuuid}
    headers = {'Authorization': f"Bearer {OAuth}",
               'Accept-Language': 'en'}
    request_body = {
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
    'weight': 5
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
],
        'same_day_data': {
            'delivery_interval': {
                'from': date_start,
                'to': date_end
                                  }
                          },
    }

    response = requests.post(url, params=params, headers=headers, json=request_body)
    print(response.text)
    order_id = response.json()['id']

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