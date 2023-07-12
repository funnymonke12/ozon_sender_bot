import requests
from config import client_id, api_key

def get_data(id, key):
    # global posting_number
    # url = 'https://api-seller.ozon.ru/v3/posting/fbs/unfulfilled/list'
    # query = {"with": {
    #             "analytics_data": True,
    #             "barcodes": True,
    #             "financial_data": True,
    #             "translit": True
    #             },
    # }
    # headers = {'Client-Id': id,
    #            'Api-Key': key}
    # response = requests.post(url, params=query, headers=headers).text
    # posts = response["result"]["postings"]
    # for post in posts:
        # delivery_status = post["status"]
        # product_data = post["products"][0]
        # product_id = product_data["offer_id"]
        # delivery_date_begin = post["analytics_data"]['delivery_date_begin']
        # delivery_date_end = post["analytics_data"]['delivery_date_end']
        # quantity = product_data['quantity']
        # price = product_data["price"]
        # customer = post["customer"]
        # first_address = ''
        # second_address = customer["address"]["address_tail"]
        # client_phone = customer["phone"]
        # comment = customer["address"]["comment"]
        # latitude = customer["address"]["latitude"]
        # longitude = customer["address"]["longitude"]
        # posting_number = post["posting_number"]
        # latitude = customer["address"]["latitude"]
        # longitude = customer["address"]["longitude"]
    posts_dict = {}
    for i in range(1, 4):
        product_data = 'Какой-то продукт'
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
        dr_comment = 'Коментарий для водителя'

        posts_dict[f'{str(i)}'] = {'data': product_data,
                                   'id': product_id,
                                   'date_begin': delivery_date_begin,
                                   'date_end': delivery_date_end,
                                   'quantity': quantity,
                                   'price': price,
                                   'customer': customer,
                                   'f_addres': first_address,
                                   's_addres': second_address,
                                   'phone': client_phone,
                                   'comment': comment,
                                   'dr_comment': dr_comment,
                                   'del_status': delivery_status,
                                   'posting_number': posting_number,
                                   'card_id': str(i)}
    return posts_dict

def get_clients_coords(id, api):
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
    # customer = posts["customer"]
    # latitude = customer["address"]["latitude"]
    # longitude = customer["address"]["longitude"]
    # return latitude, longitude
    return 57.870915, 59.948918

def write_delivering(id, api, posting_number):
    # url = 'https://api-seller.ozon.ru/v2/fbs/posting/delivering'
    # query = {'Client-Id': id,
    #          'Api-Key': api,
    #          "posting_number": posting_number}
    # requests.post(url, params=query)
    pass
def write_last_mile(id, api, posting_number):
    # url = 'https://api-seller.ozon.ru/v2/fbs/posting/last-mile'
    # query = {'Client-Id': id,
    #          'Api-Key': api,
    #          "posting_number": posting_number}
    # requests.post(url, params=query)
    pass

def write_delivered(id, api, posting_number):
    # url = 'https://api-seller.ozon.ru/v2/fbs/posting/delivered'
    # query = {'Client-Id': id,
    #          'Api-Key': api,
    #          "posting_number": posting_number}
    # requests.post(url, params=query)
    pass

def write_sended_by_seller(id, api, posting_number):
    # url = 'https://api-seller.ozon.ru/v2/fbs/posting/sent-by-seller'
    # query = {'Client-Id': id,
    #          'Api-Key': api,
    #          "posting_number": posting_number}
    # requests.post(url, params=query)
    pass

