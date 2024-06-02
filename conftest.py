import json
import allure
import pytest
import random

from faker import Faker
from scooter_api import CourierRequests


@pytest.fixture
@allure.step('Запрос для отправки заказа')
def create_data_order():
    faker = Faker()
    payload = {
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
        "address": faker.address(),
        "metroStation": random.randrange(10),
        "phone": faker.phone_number(),
        "rentTime": random.randrange(6),
        "deliveryDate": faker.date(),
        "comment": faker.text(10)
    }

    return payload


@pytest.fixture
@allure.step('Создание данных курьера')
def create_user_data():
    faker = Faker()
    data = {
        "login": faker.name(),
        "password": faker.pyint(),
        "firstName": faker.name()
    }

    return json.dumps(data)


@pytest.fixture
@allure.step('Создание курьера, логин и удаление курьера')
def create_courier_login_and_delete(create_user_payload):
    payload = create_user_payload
    response = CourierRequests.create_courier_post(payload)
    login_response = CourierRequests.login_courier_post(payload)
    CourierRequests.delete_courier(courier_id=login_response["id"])

    return login_response
