#Вадим Ситдиков 10-ая когорта - Финальный проект. Инженер по тестированию плюс
import sendler_request
import data


def positive_assert_200():
        response = sendler_request.post_new_order()
        track_number = response.json()["track"]
        response = sendler_request.get_track_body(track_number)
        assert response.status_code == 200

def test_get_order_by_track_success():
    positive_assert_200()