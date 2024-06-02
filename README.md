# Sprint_7
## Автоматизация тестирования API приложения [Яндекс.Самокат](https://qa-scooter.praktikum-services.ru/)

### Используемые технологии
- Allure
- allure-pytest
- pytest
- requests

### Запуск проекта

    pip install -r requirements.txt
    pytest -v ./tests  --alluredir=allure_results
    allure serve allure_results

### Структура проекта

###### tests - пакет с модулями автотестов:
- test_create_courier.py - Создание курьера
- test_login_courier.py - Залогинивание курьера
- test_order_create.py - Создание заказа
- test_order_list.py - Получение списка заказов

***
- conftest.py - Фикстуры pytest
- data.py - Константы тестируемых адресов
- scooter_api.py - Методы взаимодействия с API
***
- allure_results - отчеты Allure