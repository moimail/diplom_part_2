import data
import postreq
import getreq


def get_order_body(first_name):
    # Копируется словарь с телом запроса из файла data
    current_body = data.create_order.copy()
    # Изменение значения в поле firstName
    current_body["firstName"] = first_name
    # Возвращается новый словарь с нужным значением firstName
    return current_body

def test_crate_order():
    #Отправляем имя заказчика
    body = getreq.get_order_body('Барc')
    print(body)
    #Добавляем заказ
    responce = postreq.post_create_order(body)
    print(responce)
    #Смотрим ответ
    resp = responce.json()
    print('Ответ ', resp)
    #Запоминаем номер трэка
    track = resp["track"]
    print(track)
    track = str(track)
    get_order_response = getreq.get_order(track)
    print(get_order_response.text)
    #Проверяем статус
    code_req = get_order_response.status_code
    assert code_req == 200
    # Тюпин Константин, 6-я когорта — Финальный проект. Инженер по тестированию плюс