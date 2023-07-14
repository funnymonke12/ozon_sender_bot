import json

import requests
from config import client_id, api_key

def get_data(id, key):
    global posting_number
    url = 'https://api-seller.ozon.ru/v3/posting/fbs/unfulfilled/list'
    query = {'Client-Id': id,
             'Api-Key': key, }

    params = {
        "dir": "asc",
        "filter": {"cutoff_from": "2021-10-24T14:15:22Z", "cutoff_to": "2030-11-24T14:15:22Z",
                   "status": "awaiting_packaging"},
        "limit": 100,
        "offset": 0,
        "with": {
                "analytics_data": True,
                "barcodes": True,
                "financial_data": True,
                "translit": True
                }
 }

    response = requests.post(url=url, json=params, headers=query)
    posts = json.loads(response.text)["result"]['postings']
    posts = posts
    posts_dict = {}
    for i, post in enumerate(posts):
        delivery_status = post["status"]
        product_data = post["products"][0]
        product_id = product_data["offer_id"]
        delivery_date_begin = post["analytics_data"]['delivery_date_begin']
        delivery_date_end = post["analytics_data"]['delivery_date_end']
        quantity = product_data['quantity']
        price = product_data["price"]
        customer = post["customer"]
        first_address = ''
        second_address = customer["address"]["address_tail"]
        client_phone = customer["phone"]
        comment = customer["address"]["comment"]
        latitude = customer["address"]["latitude"]
        longitude = customer["address"]["longitude"]
        posting_number = post["posting_number"]
        posts_dict[str(i)] = {'delivery_status': delivery_status,
                              'product_id': product_id,
                              'delivery_date_begin': delivery_date_begin,
                              'delivery_date_end': delivery_date_end,
                              'quantity': quantity,
                              'price': price,
                              'first_addres': first_address,
                              'second_addres': second_address,
                              'client_phone': client_phone,
                              'comment': comment,
                              'posting_number': posting_number,
                              'latitude': latitude,
                              'longitude': longitude,
                              'card_id': str(i)
                              }

    return posts_dict

def get_clients_coords(card_id):
    data = get_data(client_id, api_key)
    if str(card_id) in data.keys():
        return data[str(card_id)]['latitude'], data[str(card_id)]['longitude']


def write_delivering(id, api, posting_number):
    url = 'https://api-seller.ozon.ru/v2/fbs/posting/delivering'
    query = {'Client-Id': id,
             'Api-Key': api,
             }
    params = {"posting_number": posting_number}

    requests.post(url, headers=query, json=params)

def write_last_mile(id, api, posting_number):
    url = 'https://api-seller.ozon.ru/v2/fbs/posting/last-mile'
    query = {'Client-Id': id,
             'Api-Key': api,
             }
    params = {"posting_number": posting_number}

    requests.post(url, headers=query, json=params)


def write_delivered(id, api, posting_number):
    url = 'https://api-seller.ozon.ru/v2/fbs/posting/delivered'
    query = {'Client-Id': id,
             'Api-Key': api,
             }
    params = {"posting_number": posting_number}

    requests.post(url, headers=query, json=params)


def write_sended_by_seller(id, api, posting_number):
    url = 'https://api-seller.ozon.ru/v2/fbs/posting/sent-by-seller'
    query = {'Client-Id': id,
             'Api-Key': api,
             }
    params = {"posting_number": posting_number}

    requests.post(url, headers=query, json=params)

