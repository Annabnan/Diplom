import sender_stand_request
import data

# Анна Мякишева, 23-я когорта — Финальный проект. Инженер по тестированию плюс
# Автотест: Создание и получение заказа
def test_post_and_get_order():
    # Создание нового заказа
    create_order = sender_stand_request.post_new_order(data.order_body)

    if create_order.status_code == 201:
        tracker = create_order.json().get("track")
        print(f"Заказ успешно создан. Номер трекера: {tracker}")
    else:
        print(f"Ошибка при создании заказа: {create_order.status_code}")
        return

    # Получение информации о заказе по трекеру
    get_order_track = sender_stand_request.get_order(tracker)

    assert get_order_track.ok, f"Ошибка при получении данных заказа: {get_order_track.status_code}"

    # Проверка статус-кода
    if get_order_track.status_code == 200:
        order_details = get_order_track.json()
        print("Информация о заказе:")
        print(order_details)
    else:
        print(f"Ошибка: получен статус-код {get_order_track.status_code}")