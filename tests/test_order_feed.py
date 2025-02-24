import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.order_feed_page import OrderFeedPage
from constants import URLs
from utils.api_client import APIClient


@pytest.mark.usefixtures("driver")
@allure.feature("Лента заказов")
class TestOrderFeed:
    """Тесты для раздела 'Лента заказов'"""

    @allure.story("Открытие деталей заказа")
    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_order_details_modal(self, driver):
        driver.get(URLs.BASE_URL)
        main_page = MainPage(driver)

        with allure.step("Переход в 'Ленту заказов'"):
            main_page.go_to_order_feed()

        order_feed_page = OrderFeedPage(driver)

        with allure.step("Кликаем на первый заказ"):
            order_feed_page.click_on_first_order()

        with allure.step("Проверяем, что модальное окно появилось"):
            assert order_feed_page.is_order_details_modal_visible(), "Модальное окно с деталями заказа не появилось"

    @allure.story("Проверка отображения заказов в истории и ленте")
    @allure.title("Заказы из 'Истории заказов' отображаются в 'Ленте заказов'")
    def test_orders_are_displayed_in_history_and_feed(self, driver, test_user):
        driver.get(URLs.BASE_URL)  # Открываем главную страницу
        main_page = MainPage(driver)

        with allure.step("Авторизуемся"):
            main_page.go_to_account()
            login_page = LoginPage(driver)
            login_page.enter_email(test_user["email"])
            login_page.enter_password(test_user["password"])
            login_page.click_login_button()

        with allure.step("Создаём 2 заказа"):
            main_page.create_multiple_orders(2)

        with allure.step("Переход в 'Историю заказов'"):
            main_page.go_to_account()
            account_page = AccountPage(driver)
            account_page.go_to_order_history()

        with allure.step("Получаем список номеров заказов из 'Истории заказов'"):
            history_order_numbers = account_page.get_order_numbers_from_history()

        with allure.step("Переход в 'Ленту заказов'"):
            main_page.go_to_order_feed()
            order_feed_page = OrderFeedPage(driver)

        with allure.step("Получаем список номеров заказов из 'Ленты заказов'"):
            feed_order_numbers = order_feed_page.get_order_numbers_from_feed()

        with allure.step("Проверяем, что заказы из истории есть в 'Ленте заказов'"):
            assert all(order in feed_order_numbers for order in history_order_numbers), (
                f"Не все заказы из 'Истории заказов' найдены в 'Ленте заказов'.\n"
                f"Ожидалось: {history_order_numbers}\n"
                f"Получено: {feed_order_numbers}"
            )

    @allure.story("Проверка счётчика выполненных заказов")
    @allure.title("Счётчик 'Выполнено за всё время' увеличивается при создании заказа")
    def test_completed_orders_counter_increases(self, driver, test_user):
        driver.get(URLs.BASE_URL)
        main_page = MainPage(driver)

        with allure.step("Переход в 'Ленту заказов'"):
            main_page.go_to_order_feed()

        order_feed_page = OrderFeedPage(driver)

        with allure.step("Запоминаем текущее количество выполненных заказов"):
            initial_count = order_feed_page.get_completed_orders_count()

        with allure.step("Создаём заказ через API"):
            APIClient.create_order(test_user["token"])

        with allure.step("Повторно переходим в 'Ленту заказов'"):
            main_page.go_to_order_feed()

        with allure.step("Проверяем, что счётчик увеличился на 1"):
            updated_count = order_feed_page.get_completed_orders_count()
            assert updated_count == initial_count + 1, (
                f"Счетчик заказов не увеличился. Было: {initial_count}, стало: {updated_count}"
            )

    @allure.story("Проверка счётчика выполненных заказов за сегодня")
    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается после создания заказа")
    def test_completed_orders_today_increases(self, driver, test_user):
        driver.get(URLs.BASE_URL)
        main_page = MainPage(driver)

        with allure.step("Переход в 'Ленту заказов'"):
            main_page.go_to_order_feed()

        order_feed_page = OrderFeedPage(driver)

        with allure.step("Запоминаем текущее количество выполненных заказов за сегодня"):
            initial_count = order_feed_page.get_completed_orders_count_today()

        with allure.step("Создаём заказ через API"):
            APIClient.create_order(test_user["token"])

        with allure.step("Повторно переходим в 'Ленту заказов'"):
            main_page.go_to_order_feed()

        with allure.step("Проверяем, что счётчик увеличился на 1"):
            updated_count = order_feed_page.get_completed_orders_count_today()
            assert updated_count == initial_count + 1, (
                f"Счётчик 'Выполнено за сегодня' не увеличился.\n"
                f"Было: {initial_count}, Стало: {updated_count}"
            )

    @allure.story("Проверка появления номера заказа в разделе 'В работе'")
    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_number_appears_in_progress(self, driver, test_user):
        with allure.step("Создаём заказ через API"):
            order_response = APIClient.create_order(test_user["token"])

        assert "order" in order_response and "number" in order_response["order"], (
            f"Ошибка: в ответе отсутствует номер заказа: {order_response}"
        )

        order_number = str(order_response["order"]["number"])
        allure.attach(order_number, name="Номер заказа", attachment_type=allure.attachment_type.TEXT)

        driver.get(URLs.BASE_URL)
        main_page = MainPage(driver)

        with allure.step("Переход в 'Ленту заказов'"):
            main_page.go_to_order_feed()

        order_feed_page = OrderFeedPage(driver)

        with allure.step("Проверяем, что номер заказа появился в разделе 'В работе'"):
            is_order_in_progress = order_feed_page.verification_in_progress_order_number(order_number)
            assert is_order_in_progress, (
                f"Номер заказа не найден в разделе 'В работе'.\n"
                f"Ожидалось: True\n"
                f"Получено: {is_order_in_progress}"
            )
