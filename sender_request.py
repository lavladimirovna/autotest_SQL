import requests
import Configuration
import data


def post_new_orders():
    return requests.post(Configuration.URL_SERVICE + Configuration.CREATE_ORDERS_PATH,
                         json=data.orders_body)


def get_order_info(track_number):
    return requests.get(Configuration.URL_SERVICE + Configuration.GET_ORDER,
                        params={"t": track_number})
