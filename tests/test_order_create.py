import allure
import pytest

from scooter_api import OrderApiClient


@allure.feature('Проверка создания заказа')
class TestOrderCreate:
    @allure.title('Создание заказа с различным выбором цвета самоката')
    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['BLACK', 'GREY'],
        ''])
    def test_create_order(self, color, create_data_order):
        api = OrderApiClient()
        payload = create_data_order
        response = api.create_order_post(payload)
        assert "track" in response.keys()
