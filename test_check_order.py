import data
import config
import requests

def post_create_order(body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH, json=body)

def get_order(track):
    return requests.get(config.URL_SERVICE + config.CREATE_ORDER_PATH + track)


def get_order_body(first_name):
    # Копируется словарь с телом запроса из файла data
    current_body = data.create_order.copy()
    # Изменение значения в поле firstName
    current_body["firstName"] = first_name
    # Возвращается новый словарь с нужным значением firstName
    return current_body

def test_crate_order():
    #Отправляем имя заказчика
    body = get_order_body('Барисик')
    print(body)
    #Добавляем заказ
    responce = post_create_order(body)
    print(responce)
    #Смотрим ответ
    resp = responce.json()
    print('Ответ ', resp)
    #Запоминаем номер трэка
    track = resp["track"]
    print(track)
    get_order_response = get_order(str(track))
    print(get_order_response.json())
    #Проверяем статус
    code_req = get_order_response.status_code
    assert code_req == 200