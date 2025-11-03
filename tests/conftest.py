import allure
import pytest
from api.stellar_burgers_api import StellarBurgersAPI
from helpers import generate_name, generate_password, generate_unique_email


@pytest.fixture
def user():
    """
    Создаёт уникального пользователя и возвращает словарь с токеном и данными пользователя.
    """
    with allure.step("Генерация уникальных данных пользователя"):
        name = generate_name()
        email = generate_unique_email()  # Используем гарантированно уникальный email
        password = generate_password()

    with allure.step("Создание пользователя через API"):
        response = StellarBurgersAPI.create_user(name, email, password)
        assert response.status_code == 200, f"Не удалось создать пользователя: {response.text}"

    with allure.step("Форматирование access token"):
        access_token = response.json().get("accessToken")
        if access_token and not access_token.startswith("Bearer "):
            access_token = f"Bearer {access_token}"

    return {
        "accessToken": access_token,
        "user_data": {
            "name": name,
            "email": email,
            "password": password
        }
    }