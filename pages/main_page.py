from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from constants import URLs
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Класс для работы с главной страницей"""

    def go_to_account(self):
        """Переход в личный кабинет"""
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def is_main_header_visible(self):
        """Проверяет, отображается ли заголовок главной страницы"""
        return self.is_element_visible(MainPageLocators.MAIN_HEADER)

    def go_to_order_feed(self):
        """Переход в 'Ленту заказов'"""
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    def click_on_second_ingredient(self):
        """Кликает по второму ингредиенту"""
        self.click(MainPageLocators.SECOND_INGREDIENT)

    def drag_ingredient_to_constructor(self):
        """Перетаскивает ингредиент в поле 'Состав заказа'"""
        ingredient = self.find_element(MainPageLocators.SECOND_INGREDIENT)
        constructor = self.find_element(MainPageLocators.ORDER_CONSTRUCTOR)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, constructor).perform()

    def is_ingredient_counter_visible(self):
        """Проверяет, что счетчик ингредиента увеличился"""
        return self.is_element_visible(MainPageLocators.INGREDIENT_COUNTER)

    def click_order_button(self):
        """Кликает на кнопку 'Оформить заказ'"""
        self.click(MainPageLocators.ORDER_BUTTON)

    def is_order_confirmation_visible(self):
        """Проверяет, что появилось подтверждение заказа"""
        return self.is_element_visible(MainPageLocators.ORDER_NUMBER)

    def create_order(self):
        """Создает заказ, возвращает его номер"""

        # Перетаскиваем ингредиент в конструктор
        ingredient = self.find_element(MainPageLocators.SECOND_INGREDIENT)
        constructor = self.find_element(MainPageLocators.ORDER_CONSTRUCTOR)
        ActionChains(self.driver).drag_and_drop(ingredient, constructor).perform()

        # Оформляем заказ
        self.click(MainPageLocators.ORDER_BUTTON)

        # Ожидаем обновления номера заказа в модальном окне
        order_number_element = self.find_element(MainPageLocators.ORDER_NUMBER)
        old_order_number = order_number_element.text.strip()
        self.wait_for_text_to_change(MainPageLocators.ORDER_NUMBER, old_order_number)

        """Закрывает модальное окно с двойным кликом (на случай ошибки)"""
        close_button = self.find_element(MainPageLocators.CLOSE_MODAL_BUTTON)
        try:
            close_button.click()
        except ElementClickInterceptedException:
            close_button.click()

    def create_multiple_orders(self, count):
        """Создает указанное количество заказов и возвращает их номера"""
        return [self.create_order() for _ in range(count)]

    def go_to_login_page(self):
        """Переходит на страницу 'Личный кабинет'"""
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def open_main_page(self):
        """Открывает главную страницу"""
        self.open_page(URLs.BASE_URL)
