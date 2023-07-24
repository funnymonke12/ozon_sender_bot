api_keys = [('Tropic of Trade', '1164647', 'c4bffaf0-da01-4c67-b91c-af2e7bff4a8d'),
            ('Idea Inventor', '1151381', 'be60399b-3502-453a-a8af-1e58396aa693'),
            ('Express Beast', '1227099', '3d7e45b1-ff05-44e6-9a20-3fb0e3a84258'),
            ('MetroExpress', '1218747', 'c428beb2-e90b-4a3c-8bc2-ee52b6121e87'),
            ('Express Dharma', '1217122', 'd6500f1e-d97c-4f59-ab81-f38efe30c877'),
            ('Mario Cart', '1267379', '094bf0ae-3d15-4813-995a-b838da191535'),
            ('ИП УКОЛОВ', '1246235', 'bece440d-2221-42e5-b744-53d2a470d23c'),
            ('Tactical Gear Hub', '1248044', 'c88bd6f1-6b9d-4272-aa7a-646126f059ec')]
bot_api = '6316834487:AAFQZIuEjZsxw8KGp5w8ADTUTYAtder5W3w'
OAuth = 'y0_AgAAAABklX-XAAc6MQAAAADXUf2CHF3GQ268RMGJeXJSNx-otX3SVgk'
geocoder_key = '0567c4eb-ead9-4521-87ab-2adecfa15d1a'

response = {
"result": {
"postings": [
{
"posting_number": "23713478-0018-3",
"order_id": 559293114,
"order_number": "33713378-0051",
"status": "awaiting_packaging",
"delivery_method": {
"id": 15110442724000,
"name": "Ozon Логистика курьеру, Москва",
"warehouse_id": 15110442724000,
"warehouse": "Склад на Ленина",
"tpl_provider_id": 24,
"tpl_provider": "Ozon Логистика"
},
"tracking_number": "",
"tpl_integration_type": "ozon",
"in_process_at": "2021-08-25T10:48:38Z",
"shipment_date": "2021-08-26T10:00:00Z",
"delivering_date": 'Дата передачи отправления в доставку',
"cancellation": {
"cancel_reason_id": 0,
"cancel_reason": "",
"cancellation_type": "",
"cancelled_after_ship": False,
"affect_cancellation_rating": False,
"cancellation_initiator": ""
},
"customer": {"address": {"comment": 'Коментарий клиента',
                         'latitude': '55.751254',
                         'longitude': '37.597432',
                         'address_tail': 'улица Арбат, 13, Москва'
                         }
            },
"products": [
{
"price": "1259",
"currency_code": "RUB",
"offer_id": "УТ-0001365",
"name": "Мяч, цвет: черный, 5 кг",
"sku": 140048123,
"quantity": 1,
"products_requiring_jw_uin": "0",
"mandatory_mark": [ ]
}
],
"addressee": None,
"barcodes": {
"upper_barcode": "%101%806044518",
"lower_barcode": "23024930500000"
},
"analytics_data": {
"region": "Санкт-Петербург",
"city": "Санкт-Петербург",
"delivery_type": "PVZ",
"is_premium": False,
"payment_type_group_name": "Карты оплаты",
"warehouse_id": 15110442724000,
"warehouse": "Склад на Ленина",
"tpl_provider_id": 24,
"tpl_provider": "Ozon Логистика",
"delivery_date_begin": "2022-08-28T14:00:00Z",
"delivery_date_end": "2022-08-28T18:00:00Z",
"is_legal": None
},
"financial_data": {
"products": [
{
"commission_amount": 0,
"commission_percent": 0,
"payout": 0,
"product_id": 140048123,
"old_price": 1888,
"price": 1259,
"total_discount_value": 629,
"total_discount_percent": 33.32,
"actions": [
"Системная виртуальная скидка селлера"
],
"picking": None,
"quantity": 1,
"client_price": "",
"item_services": {
"marketplace_service_item_fulfillment": 0,
"marketplace_service_item_pickup": 0,
"marketplace_service_item_dropoff_pvz": 0,
"marketplace_service_item_dropoff_sc": 0,
"marketplace_service_item_dropoff_ff": 0,
"marketplace_service_item_direct_flow_trans": 0,
"marketplace_service_item_return_flow_trans": 0,
"marketplace_service_item_deliv_to_customer": 0,
"marketplace_service_item_return_not_deliv_to_customer": 0,
"marketplace_service_item_return_part_goods_customer": 0,
"marketplace_service_item_return_after_deliv_to_customer": 0
}
}
],
"posting_services": {
"marketplace_service_item_fulfillment": 0,
"marketplace_service_item_pickup": 0,
"marketplace_service_item_dropoff_pvz": 0,
"marketplace_service_item_dropoff_sc": 0,
"marketplace_service_item_dropoff_ff": 0,
"marketplace_service_item_direct_flow_trans": 0,
"marketplace_service_item_return_flow_trans": 0,
"marketplace_service_item_deliv_to_customer": 0,
"marketplace_service_item_return_not_deliv_to_customer": 0,
"marketplace_service_item_return_part_goods_customer": 0,
"marketplace_service_item_return_after_deliv_to_customer": 0
}
},
"is_express": False,
"requirements": {
"products_requiring_gtd": [ ],
"products_requiring_country": [ ],
"products_requiring_jwn": [ ]
}
}
],
"count": 55
}
}



