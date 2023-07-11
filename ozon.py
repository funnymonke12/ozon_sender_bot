import requests
from config import client_id, api_key

def get_data(id, key):
    # url = 'https://api-seller.ozon.ru/v3/posting/fbs/unfulfilled/list'
    # params = {"with": {
    #             "analytics_data": True,
    #             "barcodes": True,
    #             "financial_data": True,
    #             "translit": True
    #             },
    #     'Client-Id': client_id,
    #     'Api-Key': api_key
    # }
    # response = requests.post(url, params).text
    # posts = response["result"]["postings"][0]
    # product_data = posts["products"][0]
    # product_id = product_data["offer_id"]
    # delivery_date_begin = posts["analytics_data"]['delivery_date_begin']
    # delivery_date_end = posts["analytics_data"]['delivery_date_end']
    # quantity = product_data['quantity']
    # price = product_data["price"]
    # customer = posts["customer"]
    # first_address = ''
    # second_address = customer["address"]["address_tail"]
    # client_phone = customer["phone"]
    # comment = customer["address"]["comment"]
    # latitude = customer["address"]["latitude"]
    # longitude = customer["address"]["longitude"]
    return '123', '12.03.2022-28.04.2023', '3', '1059', '', 'yl pyshkina', '+79834', 'comment', 'comment_dr'


