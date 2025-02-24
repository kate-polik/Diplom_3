from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    """Page Object страницы 'Лента заказов'"""

    def is_order_feed_header_visible(self):
        """Проверяет, отображается ли заголовок 'Лента заказов'"""
        return self.is_element_visible(OrderFeedLocators.ORDER_FEED_HEADER)

    def click_on_first_order(self):
        """Кликает на первый заказ в ленте заказов"""
        self.click(OrderFeedLocators.FIRST_ORDER)

    def is_order_details_modal_visible(self):
        """Проверяет, что модальное окно с деталями заказа открылось"""
        return self.is_element_visible(OrderFeedLocators.ORDER_DETAILS_MODAL)

    def get_order_numbers_from_feed(self):
        """Возвращает список номеров заказов из 'Истории заказов'"""
        order_elements = self.driver.find_elements(*OrderFeedLocators.ORDER_NUMBERS_LOCATOR_HISTORY)
        return [order.text for order in order_elements if order.text.startswith("#0")]

    def get_completed_orders_count(self):
        """Получает текущее количество выполненных заказов"""
        count_element = self.find_element(OrderFeedLocators.COMPLETED_ORDERS_COUNT)
        return int(count_element.text)

    def get_completed_orders_count_today(self):
        """Получает текущее количество выполненных заказов за сегодня"""
        return int(self.find_element(OrderFeedLocators.COMPLETED_ORDERS_COUNT_TODAY).text)

    def verification_in_progress_order_number(self, order_number):
        """Получает номер заказа в разделе 'В работе'"""
        return self.wait_for_text_in_element(OrderFeedLocators.IN_PROGRESS_ORDERS, order_number)
