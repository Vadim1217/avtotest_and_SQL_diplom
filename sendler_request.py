import configuration
import requests
import data

def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PACH,
                         json=data.order_body
                         )



def get_track_body():
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_TRACK_PACH + str(post_new_order().json()["track"]))
print(get_track_body().json())