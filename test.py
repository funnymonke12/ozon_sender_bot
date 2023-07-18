import requests

from config import OAuth

url = 'https://b2b.taxi.yandex.net/b2b/cargo/integration/v2/claims/info'
params = {'claim_id': '6b2835449f4247cabe3e367269394812'}
headers = {'Authorization': f"Bearer {OAuth}",
           'Accept-Language': 'en'}
# request_body = {'cancel_state': 'free',
#                 'version': 2}
response = requests.post(url, params=params, headers=headers)
print(response)
print(response.text)