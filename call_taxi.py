import requests

def call_taxi(start_lat, start_lon, end_lat, end_lon):
    url = f'https://3.redirect.appmetrica.yandex.com/route?start-lat={start_lat}&start-lon={start_lon}&end-lat={end_lat}&end-lon={end_lon}&level=econom&ref=telegram_bot&appmetrica_tracking_id=25395763362139037'
    return url
# start-lat=<широта>
# &start-lon=<долгота>
# &end-lat=<широта>
# &end-lon=<долгота>
# &level=<тариф>
# &ref=<источник>
# &appmetrica_tracking_id=<идентификатор_перенаправления>
# &lang=<язык>)

