import configuration
import requests
import data

def posts_creating_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATING_ORDERS,
                         json=body)
response = posts_creating_orders(data.orders_body)

number = response.json()

trak = number['track']

def get_receirve_orders_number():
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDER_NUMBER + "?t=" + str(trak))