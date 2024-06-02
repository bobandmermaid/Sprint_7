import allure

from scooter_api import OrderApiClient


class TestOrderList:

    @allure.title('Проверка получения списка заказов')
    def test_order_list(self):
        api = OrderApiClient()
        response = api.get_orders_list()
        assert "orders" in response.keys()
