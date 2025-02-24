import pytest
import allure
from constants import URLs, TestUserData
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators


@pytest.mark.usefixtures("driver")
@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.story("Переход на страницу восстановления пароля")
    @allure.title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_navigate_to_password_recovery(self, driver):
        """Тест: Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'."""
        driver.get(URLs.BASE_URL)

        with allure.step("Переход на страницу 'Восстановление пароля'"):
            LoginPage(driver).go_to_password_recovery()

        recovery_page = PasswordRecoveryPage(driver)

        with allure.step("Ожидаем появления заголовка 'Восстановление пароля'"):
            header_element = recovery_page.wait_for_password_recovery_header()

        with allure.step("Проверяем, что заголовок отображается"):
            assert header_element.is_displayed(), "Заголовок 'Восстановление пароля' не найден на странице"

    @allure.story("Ввод почты и отправка запроса на восстановление пароля")
    @allure.title("Ввод почты и клик по кнопке 'Восстановить'")
    def test_enter_email_and_submit_recovery(self, driver):
        """Тест: Ввод почты и клик по кнопке 'Восстановить'."""
        driver.get(URLs.BASE_URL)

        with allure.step("Переход на страницу 'Восстановление пароля'"):
            LoginPage(driver).go_to_password_recovery()

        recovery_page = PasswordRecoveryPage(driver)

        with allure.step("Ожидаем появления заголовка 'Восстановление пароля'"):
            header_element = recovery_page.wait_for_password_recovery_header()

        with allure.step("Вводим email и отправляем запрос на восстановление"):
            recovery_page.enter_email(TestUserData.TEST_EMAIL)
            recovery_page.click_recover()

        with allure.step("Проверяем, что заголовок всё ещё отображается после отправки формы"):
            assert header_element.is_displayed(), "Заголовок 'Восстановление пароля' пропал после отправки формы"

    @allure.story("Показ/скрытие пароля делает поле активным")
    @allure.title("Клик по кнопке 'Показать/скрыть пароль' делает поле активным")
    def test_toggle_password_visibility_activates_field(self, driver):
        """Тест: Клик по кнопке 'Показать/скрыть пароль' делает поле активным."""
        driver.get(URLs.BASE_URL)

        with allure.step("Переход на страницу 'Восстановление пароля'"):
            LoginPage(driver).go_to_password_recovery()

        recovery_page = PasswordRecoveryPage(driver)

        with allure.step("Вводим email и отправляем запрос на восстановление"):
            recovery_page.enter_email(TestUserData.TEST_EMAIL)
            recovery_page.click_recover()

        with allure.step("Нажимаем на кнопку 'Показать/скрыть пароль'"):
            recovery_page.toggle_password_visibility()

        with allure.step("Проверяем, что поле пароля стало активным"):
            assert recovery_page.wait_for_element(PasswordRecoveryPageLocators.PASSWORD_INPUT_ACTIVE).is_displayed(), (
                "Поле пароля не стало активным после нажатия кнопки 'Показать/скрыть пароль'"
            )
