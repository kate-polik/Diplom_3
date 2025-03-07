import pytest
import allure
from pages.main_page import MainPage
from pages.ingredient_modal_page import IngredientModal
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage


@pytest.mark.usefixtures("driver")
@allure.feature("Основной функционал")
class TestMainFunctionality:
    """Тесты основного функционала"""

    @allure.story("Переход в Конструктор")
    @allure.title("Переход по клику на 'Конструктор'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_constructor(self, driver):
        """Тест: Переход по клику на 'Конструктор'"""
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Кликаем на 'Личный кабинет'"):
            main_page.go_to_account()

        with allure.step("Кликаем 'Конструктор'"):
            login_page = LoginPage(driver)
            login_page.go_to_constructor()

        with allure.step("Проверяем, что перешли в 'Конструктор'"):
            assert main_page.is_main_header_visible(), "Не удалось перейти в 'Конструктор'"

    @allure.story("Переход в Ленту заказов")
    @allure.title("Переход по клику на 'Лента заказов'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_order_feed(self, driver):
        """Тест: Переход по клику на 'Лента заказов'"""
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Кликаем 'Лента заказов'"):
            main_page.go_to_order_feed()

        with allure.step("Проверяем, что перешли в 'Ленту заказов'"):
            order_feed_page = OrderFeedPage(driver)
            assert order_feed_page.is_order_feed_header_visible(), "Не удалось перейти в 'Ленту заказов'"

    @allure.story("Просмотр деталей ингредиента")
    @allure.title("Клик по ингредиенту открывает всплывающее окно с деталями")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ingredient_modal(self, driver):
        """Тест: если кликнуть на ингредиент, появится всплывающее окно с деталями"""
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Кликаем на ингредиент"):
            main_page.click_on_second_ingredient()

        ingredient_modal = IngredientModal(driver)

        with allure.step("Проверяем, что открылось модальное окно с деталями"):
            assert ingredient_modal.is_ingredient_modal_open(), "Модальное окно ингредиента не открылось"

    @allure.story("Закрытие всплывающего окна ингредиента")
    @allure.title("Всплывающее окно ингредиента закрывается по клику на крестик")
    @allure.severity(allure.severity_level.NORMAL)
    def test_close_ingredient_modal(self, driver):
        """Тест: всплывающее окно закрывается кликом по крестику"""
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Открываем ингредиент"):
            main_page.click_on_second_ingredient()

        with allure.step("Закрываем модальное окно"):
            ingredient_modal = IngredientModal(driver)
            ingredient_modal.close_modal()

        with allure.step("Проверяем, что модальное окно закрылось"):
            assert ingredient_modal.is_ingredient_modal_closed(), "Модальное окно ингредиента не закрылось"

    @allure.story("Добавление ингредиента в заказ")
    @allure.title("При добавлении ингредиента в заказ увеличивается счетчик")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ingredient_counter_increases(self, driver):
        """Тест: при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента"""
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Добавляем ингредиент в заказ"):
            main_page.drag_ingredient_to_constructor()

        with allure.step("Проверяем, что счетчик увеличился"):
            assert main_page.is_ingredient_counter_visible(), "Счетчик ингредиента не увеличился"

    @allure.story("Оформление заказа")
    @allure.title("Залогиненный пользователь может оформить заказ")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_logged_in_user_can_place_order(self, driver, test_user):
        """Тест: залогиненный пользователь может оформить заказ"""
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Переход в 'Личный кабинет' для авторизации"):
            main_page.go_to_account()

        with allure.step("Ввод email и пароля"):
            login_page = LoginPage(driver)
            login_page.enter_email(test_user["email"])
            login_page.enter_password(test_user["password"])
            login_page.click_login_button()

        with allure.step("Добавляем ингредиент в заказ"):
            main_page.drag_ingredient_to_constructor()

        with allure.step("Оформляем заказ"):
            main_page.click_order_button()

        with allure.step("Проверяем, что появилось подтверждение заказа"):
            assert main_page.is_order_confirmation_visible(), "Не появилось подтверждение заказа"

