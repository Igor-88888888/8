import sender_stand_request

def test1_positive_receiving_order_by_track():

    response_get = sender_stand_request.get_receirve_orders_number()

    assert response_get.status_code == 200

# Игорь Мирошников, 16-я когорта — Финальный проект. Инженер по тестированию плюс

