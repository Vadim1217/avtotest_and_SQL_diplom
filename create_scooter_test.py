#Вадим Ситдиков 10-ая когорта - Финальный проект. Инженер по тестированию плюс
import sendler_request
import data


def positive_assert_200():
        response = sendler_request.get_track_body()
        assert response.status_code == 200

def test_positive_200():
    positive_assert_200()