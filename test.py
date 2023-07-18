import requests

from config import OAuth

url = 'https://b2b.taxi.yandex.net/b2b/cargo/integration/v2/claims/info'
params = {'claim_id': 'bd6b9efd56d14fd19faa4ae9e1c1d6aa'}
headers = {'Authorization': f"Bearer {OAuth}",
           'Accept-Language': 'en'}
request_body = {}
response = requests.post(url, params=params, headers=headers, json=request_body)
print(response)
print(response.text)