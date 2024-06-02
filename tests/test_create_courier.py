import json

import allure
import pytest

from scooter_api import CourierRequests


@allure.feature('Проверка регистрации курьера')
class TestCreateCourier:

    @allure.title('Проверяем, что курьера можно создать')
    def test_registration_login(self, create_user_data):
        courier_requests = CourierRequests()
        response = courier_requests.create_courier_post(create_user_data)
        assert response['ok']

    @allure.title('Проверяем, что нельзя создать двух одинаковых курьеров')
    def test_duplicate_courier(self, create_user_data):
        courier_requests = CourierRequests()
        payload = create_user_data
        courier_requests.create_courier_post(payload)
        response = courier_requests.login_courier_post(payload)
        response_double = courier_requests.create_courier_post(payload, status=409)
        courier_id = response["id"]
        courier_requests.delete_courier(courier_id=courier_id)
        assert response_double["message"] == "Этот логин уже используется. Попробуйте другой."

    @pytest.mark.parametrize("payload_data",
                             [
                                 ['', '0000', 'Иван'],
                                 ['kolo', '', 'Боб'],
                                 ['', '', 'Нина'],
                                 ['', '0987', ''],
                                 ['kilo', '', '']
                             ])
    @allure.title('Проверка, что без обязательных данных (логин, пароль) курьер не создается')
    def test_required_fields_on_register(self, payload_data):
        courier_requests = CourierRequests()
        payload = json.dumps(payload_data)
        response = courier_requests.create_courier_post(payload, status=400)
        assert response["message"] == "Недостаточно данных для создания учетной записи"
