import requests
import configuration


# Функция для создания заказа
def post_new_order(data):
    url = f"{configuration.URL_SERVICE}{configuration.ORDER_CREATE_PATH}"
    response = requests.post(url, json=data)
    return response

# Функция для получения заказа по номеру трекера
def get_order(tracker):
    url = f"{configuration.URL_SERVICE}{configuration.ORDER_GET_PATH}"
    params = {"t": tracker}
    response = requests.get(url, params=params)
    return response
