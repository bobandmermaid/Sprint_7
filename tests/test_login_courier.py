import allure
import pytest

from scooter_api import CourierRequests


@allure.feature('Проверка авторизации курьеров')
class TestLoginCourier:
    @allure.title('Успешный логин курьера')
    def test_login(self, create_courier_login_and_delete):
        response = create_courier_login_and_delete
        assert response.get('id') is not None

    @pytest.mark.parametrize("login, password", [('Боб Дилан', ''), ('', '0987'),])
    @allure.title('Проверка, что без одного обязательного поля (логин или пароль) курьер не входит')
    def test_required_fields_on_login(self, login, password):
        courier_requests = CourierRequests()
        payload = courier_requests.create_login_data(login, password)
        response = courier_requests.login_courier_post(payload, status=400)
        assert response['message'] == 'Недостаточно данных для входа'

    @allure.title('Курьер не может войти с неверным паролем')
    def test_login(self):
        courier_requests = CourierRequests()
        payload = courier_requests.create_login_data('Боб Дилан', '09876')
        response = courier_requests.login_courier_post(payload, status=404)
        assert response['message'] == 'Учетная запись не найдена'

    @allure.title('Курьер, сначала созданный а потом удаленный, не может войти в систему')
    def test_courier_cant_login_after_deleting_account(self, create_user_data):
        courier_requests = CourierRequests()
        payload = create_user_data
        courier_requests.create_courier_post(payload)
        response = courier_requests.login_courier_post(payload)
        courier_id = response["id"]
        response_delete = courier_requests.delete_courier(courier_id=courier_id)
        assert response_delete['ok']
        response = courier_requests.login_courier_post(payload, status=404)
        assert response["message"] == "Учетная запись не найдена"
