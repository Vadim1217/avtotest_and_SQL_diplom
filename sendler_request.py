import configuration
import requests
import data

def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PACH,
                         json=data.order_body
                         )

def get_track_body(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_TRACK_PACH + str(track_number))
