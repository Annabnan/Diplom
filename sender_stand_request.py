import configuration
import requests
import data


def post_new_order(body):  # запрос на создание нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.ORDER_CREATE_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)
response = post_new_order(data.order_body)

# Вывод HTTP-статус кода ответа на запрос
# Код состояния указывает на результат обработки запроса сервером
track = response.json().get('track')
print(track)

def get_order(track):
    url = f"{configuration.URL_SERVICE}{configuration.ORDER_GET_PATH}?t={track}"  # формируем полный URL
    return requests.get(url)  # выполняем GET-запр

# Вызываем функцию get_docs и сохраняем результат в переменную response
response1 = get_order(track)

# Выводим в консоль HTTP-статус код полученного ответа
# Например, 200 означает успешный запрос, 404 - не найдено и т.д.
print(response1.status_code)
if response1.status_code == 200:
    order_data = response1.json()
    print("Данные заказа:", order_data)
else:
    print("Ошибка:", response1.json())
