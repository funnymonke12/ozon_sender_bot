import json

import requests
from config import api_keys

posts_dict = {}
def get_data():
    global posting_number
    global posts_dict
    posts_dict = {}
    i = 0
    for api_key in api_keys:
        url = 'https://api-seller.ozon.ru/v3/posting/fbs/unfulfilled/list'
        query = {'Client-Id': api_key[1],
                 'Api-Key': api_key[2], }

        params = {
            "dir": "asc",
            "filter": {"cutoff_from": "2021-10-24T14:15:22Z", "cutoff_to": "2030-11-24T14:15:22Z"},
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

        for post in posts:
            delivery_status = post["status"]
            product_data = post["products"][0]
            product_name = product_data["name"]
            product_id = product_data["offer_id"]
            delivery_date_begin = f"{post['analytics_data']['delivery_date_begin'].split('T')[0][5::]}   {post['analytics_data']['delivery_date_begin'].split('T')[1][:-1]}"
            delivery_date_end = f"{post['analytics_data']['delivery_date_end'].split('T')[0][5::]}   {post['analytics_data']['delivery_date_end'].split('T')[1][:-1]}"
            quantity = product_data['quantity']
            price = product_data["price"]
            customer = post["customer"]
            second_address = customer["address"]["address_tail"]
            comment = customer["address"]["comment"]
            latitude = customer["address"]["latitude"]
            longitude = customer["address"]["longitude"]
            posting_number = post["posting_number"]
            posts_dict[str(i)] = {'delivery_status': delivery_status,
                                  'product_name': product_name,
                                  'product_id': product_id,
                                  'delivery_date_begin': delivery_date_begin,
                                  'delivery_date_end': delivery_date_end,
                                  'quantity': quantity,
                                  'price': price,
                                  'second_address': second_address,
                                  'comment': comment,
                                  'posting_number': posting_number,
                                  'latitude': latitude,
                                  'longitude': longitude,
                                  'card_id': str(i),
                                  'shop': api_key[0],
                                  'client_id': api_key[1],
                                  'api_key': api_key[2]
                                  }
            i += 1
    print(posts_dict)
    return posts_dict

def get_clients_coords(card_id):
    data = posts_dict
    if str(card_id) in data.keys():
        print(data[str(card_id)]['latitude'], data[str(card_id)]['longitude'])
        return data[str(card_id)]['latitude'], data[str(card_id)]['longitude']

def get_clients_data(card_id):
    data = posts_dict
    return data[str(card_id)]

def do_request(url, card_id):
    headers = {'Client-Id': get_clients_data(card_id)['client_id'],
             'Api-Key': get_clients_data(card_id)['api_key']}
    body = {'posting_number': get_clients_data(card_id)['posting_number']}
    requests.post(url, headers=headers, json=body)
def write_delivering(card_id):
    url = 'https://api-seller.ozon.ru/v2/fbs/posting/delivering'
    do_request(url, card_id)

def write_last_mile(card_id):
    url = 'https://api-seller.ozon.ru/v2/fbs/posting/last-mile'
    do_request(url, card_id)

def write_delivered(card_id):
    url = 'https://api-seller.ozon.ru/v2/fbs/posting/delivered'
    do_request(url, card_id)

def write_sended_by_seller(card_id):
    url = 'https://api-seller.ozon.ru/v2/fbs/posting/sent-by-seller'
    do_request(url, card_id)

