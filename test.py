# Анастасия Леухина, 6-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_request


def track_number_order():
    track_number = sender_request.post_new_orders()
    return track_number.json()["track"]


def test_track():
    track_number = track_number_order()
    get_response = sender_request.get_order_info(track_number)
    assert get_response.status_code == 200
