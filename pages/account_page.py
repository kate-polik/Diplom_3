from constants import URLs
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):
    """Класс для работы с личным кабинетом"""

    def go_to_order_history(self):
        self.click(AccountPageLocators.ORDER_HISTORY_TAB)

    def logout(self):
        self.click(AccountPageLocators.LOGOUT_BUTTON)

    def get_order_numbers_from_history(self):
        """Возвращает список номеров заказов из 'Истории заказов'"""
        order_elements = self.driver.find_elements(*AccountPageLocators.ORDER_NUMBERS_LOCATOR_ACCOUNT)
        return [order.text for order in order_elements if order.text.startswith("#0")]

    def is_order_history_open(self):
        """Проверяет, открыт ли раздел 'История заказов'"""
        return self.get_current_url() == URLs.ORDER_HISTORY
