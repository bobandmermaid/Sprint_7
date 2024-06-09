import allure
import pytest

from scooter_api import CourierRequests
from faker import Faker


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
        response_double = courier_requests.create_courier_post(payload, status=409)
        assert response_double["message"] == "Этот логин уже используется. Попробуйте другой."

    @pytest.mark.parametrize('payload_data', ['login', 'password'])
    @allure.title('Проверка ошибки при создании курьера без обязательного поля')
    def test_required_fields_on_register(self, payload_data):
        courier_requests = CourierRequests()
        faker = Faker()

        payload = {
            "login": faker.name(),
            "password": faker.pyint(),
            "firstName": faker.name()
        }
        del payload[payload_data]

        response = courier_requests.create_courier_post(payload, status=400)
        assert response["message"] == "Недостаточно данных для создания учетной записи"
