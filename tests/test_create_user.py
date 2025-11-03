import allure
import pytest
from api.stellar_burgers_api import StellarBurgersAPI
from helpers import generate_name, generate_password, generate_unique_email


class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    @allure.description("Тест проверяет успешное создание нового пользователя")
    def test_create_unique_user(self):
        with allure.step("Генерация тестовых данных"):
            name = generate_name()
            email = generate_unique_email()  # Используем гарантированно уникальный email
            password = generate_password()

        with allure.step("Отправка запроса на создание пользователя"):
            response = StellarBurgersAPI.create_user(name, email, password)

        with allure.step("Проверка успешного создания пользователя"):
            assert response.status_code == 200
            assert response.json()["success"] is True
            assert "accessToken" in response.json()

    @allure.title("Создание уже существующего пользователя")
    @allure.description("Тест проверяет обработку попытки создания дубликата пользователя")
    def test_create_existing_user(self):
        with allure.step("Генерация тестовых данных"):
            name = generate_name()
            email = generate_unique_email()  # Используем гарантированно уникальный email
            password = generate_password()
        
        with allure.step("Первое создание пользователя"):
            first_response = StellarBurgersAPI.create_user(name, email, password)
            assert first_response.status_code == 200

        with allure.step("Попытка создания пользователя с теми же данными"):
            second_response = StellarBurgersAPI.create_user(name, email, password)

        with allure.step("Проверка ошибки дублирования пользователя"):
            assert second_response.status_code == 403
            assert second_response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательного поля")
    @allure.description("Тест проверяет валидацию обязательных полей при создании пользователя")
    def test_create_user_missing_field(self):
        with allure.step("Генерация тестовых данных с пустым паролем"):
            name = generate_name()
            email = generate_unique_email()  # Используем гарантированно уникальный email
            password = ""  # не заполняем пароль

        with allure.step("Отправка запроса с отсутствующим полем"):
            response = StellarBurgersAPI.create_user(name, email, password)

        with allure.step("Проверка ошибки валидации"):
            assert response.status_code == 403
            assert response.json()["message"] == "Email, password and name are required fields"