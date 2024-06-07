import json
import allure
import pytest
import random

from faker import Faker
from scooter_api import CourierRequests


@pytest.fixture
@allure.step('Данные для заказа')
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
@allure.step('Создание курьера, логин и удаление')
def create_courier_login_and_delete(create_user_data):
    courier_requests = CourierRequests()
    payload = courier_requests.create_courier_post(create_user_data)
    response = payload
    yield response
    courier_id = response["id"]
    CourierRequests.delete_courier(courier_id=courier_id)
