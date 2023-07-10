import requests
from config import client_id, api_key

def get_data():
    requests.post('https://api-seller.ozon.ru/v3/posting/fbs/unfulfilled/list')
