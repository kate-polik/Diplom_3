import shutil
import os
from utils.browser_factory import BrowserFactory
import pytest
from utils.api_client import APIClient
from constants import URLs
from utils.data_generator import generate_user


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    driver = BrowserFactory.get_browser(browser)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def test_user():
    """Создаёт тестового пользователя перед тестом и удаляет его после теста"""
    user = generate_user()
    response = APIClient.post(URLs.REGISTER, user)
    token = response.json().get("accessToken")

    # Добавляем email и пароль
    user.update({
        "token": token,
        "email": response.json()["user"]["email"],
        "name": response.json()["user"]["name"],
        "password": user["password"]
    })

    yield user  # Передаём данные пользователя в тест

    # Удаляем пользователя
    headers = {"Authorization": user["token"]}
    APIClient.delete(URLs.USER, headers=headers)


# Хук для очистки allure_results
def pytest_sessionstart(session):
    """Очистка папки allure_results перед запуском тестов."""
    results_dir = "allure_results"
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)
    os.makedirs(results_dir)
