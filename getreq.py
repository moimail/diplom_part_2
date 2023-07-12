import data
import config
import requests


def get_order_body(first_name):
    # Копируется словарь с телом запроса из файла data
    current_body = data.create_order.copy()
    # Изменение значения в поле firstName
    current_body["firstName"] = first_name
    # Возвращается новый словарь с нужным значением firstName
    return current_body

def get_order(track):
    return requests.get(config.URL_SERVICE + config.GET_ORDER + str(track))