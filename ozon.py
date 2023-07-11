import requests
from config import client_id, api_key

def get_data(id, key):
    global posting_number
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
    # delivery_status = posts["status"]
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
    # posting_number = posts["posting_number"]
    product_data = 'Какой-то продук'
    product_id = 'Айди'
    delivery_date_begin = 'Начало даты'
    delivery_date_end = 'Конец даты'
    quantity = 'Количество'
    price = 'цена'
    customer = 'Информация клиента'
    first_address = 'адрес управляющего ботом'
    second_address = 'Адресс клиента'
    client_phone = 'Телефон клиента'
    comment = 'Комментарий клиента'
    dr_comment = 'Комментарий для водителя'
    delivery_status = "awaiting_packaging"
    posting_number = 'Номер поставки'
    # latitude = customer["address"]["latitude"]
    # longitude = customer["address"]["longitude"]'comment_dr'
    return product_id, delivery_date_begin, delivery_date_end, quantity, price, first_address, second_address, client_phone, comment, dr_comment, delivery_status, posting_number

def get_posting_number(id, api):
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
    # posting_number = posts["posting_number"]
    # return posting_number
    pass
def write_delivering(id, api):
    # url = 'https://api-seller.ozon.ru/v2/fbs/posting/delivering'
    # query = {'Client-Id': id,
    #          'Api-Key': api,
    #          "posting_number": [get_posting_number(client_id, api_key)]}
    # requests.post(url, params=query)
    pass
def write_last_mile(id, api):
    # url = 'https://api-seller.ozon.ru/v2/fbs/posting/last-mile'
    # query = {'Client-Id': id,
    #          'Api-Key': api,
    #          "posting_number": [get_posting_number(client_id, api_key)]}
    # requests.post(url, params=query)
    pass

def write_delivered(id, api):
    # url = 'https://api-seller.ozon.ru/v2/fbs/posting/delivered'
    # query = {'Client-Id': id,
    #          'Api-Key': api,
    #          "posting_number": [get_posting_number(client_id, api_key)]}
    # requests.post(url, params=query)
    pass

def write_sended_by_seller(id, api):
    # url = 'https://api-seller.ozon.ru/v2/fbs/posting/sent-by-seller'
    # query = {'Client-Id': id,
    #          'Api-Key': api,
    #          "posting_number": [get_posting_number(client_id, api_key)]}
    # requests.post(url, params=query)
    pass

