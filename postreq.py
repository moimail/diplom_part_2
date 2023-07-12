import config
import requests

def post_create_order(body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH, json=body)
