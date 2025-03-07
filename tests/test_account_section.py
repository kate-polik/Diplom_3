import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage


@pytest.mark.usefixtures("driver")
@allure.feature("Личный кабинет")
class TestAccountSection:
    """Тесты раздела 'Личный кабинет'"""

    @allure.story("Переход в личный кабинет")
    @allure.title("Переход по клику на 'Личный кабинет'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_account(self, driver):
        """Тест: Переход по клику на 'Личный кабинет'"""
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Кликаем 'Личный кабинет'"):
            main_page.go_to_account()

        with allure.step("Проверяем, что открылось окно входа"):
            login_page = LoginPage(driver)
            assert login_page.is_login_header_visible(), "Не отображается заголовок 'Вход'"

    @allure.story("Просмотр истории заказов")
    @allure.title("Переход в раздел 'История заказов'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_order_history(self, driver, test_user):
        """Тест: Переход в раздел 'История заказов'"""
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Кликаем 'Личный кабинет'"):
            main_page.go_to_account()

        with allure.step("Авторизуемся под тестовым пользователем"):
            login_page = LoginPage(driver)
            login_page.enter_email(test_user["email"])
            login_page.enter_password(test_user["password"])
            login_page.click_login_button()

        with allure.step("Снова переходим в 'Личный кабинет'"):
            main_page.go_to_account()

        with allure.step("Переходим в 'Историю заказов'"):
            account_page = AccountPage(driver)
            account_page.go_to_order_history()

        with allure.step("Проверяем, что открылась 'История заказов'"):
            assert account_page.is_order_history_open(), "Не удалось открыть 'Историю заказов'"

    @allure.story("Выход из аккаунта")
    @allure.title("Выход из личного кабинета")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_logout(self, driver, test_user):
        """Тест: Выход из аккаунта"""
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Кликаем 'Личный кабинет'"):
            main_page.go_to_account()

        with allure.step("Авторизуемся под тестовым пользователем"):
            login_page = LoginPage(driver)
            login_page.enter_email(test_user["email"])
            login_page.enter_password(test_user["password"])
            login_page.click_login_button()

        with allure.step("Снова переходим в 'Личный кабинет'"):
            main_page.go_to_account()

        with allure.step("Нажимаем 'Выход'"):
            account_page = AccountPage(driver)
            account_page.logout()

        with allure.step("Проверяем, что произошел выход из аккаунта"):
            assert login_page.is_login_header_visible(), "Не произошло выхода из аккаунта"
