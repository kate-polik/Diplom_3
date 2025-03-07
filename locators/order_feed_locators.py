from selenium.webdriver.common.by import By


class OrderFeedLocators:
    """Локаторы страницы 'Лента заказов''"""
    ORDER_FEED_HEADER = (By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-5']")
    ORDER_BY_NUMBER = lambda order_number: (By.XPATH, f"//p[contains(text(),'#0{order_number}')]")
    ORDER_DETAILS_MODAL = (
        By.XPATH, "//p[@class='text text_type_main-medium mb-8']")

    ORDER_NUMBERS_LOCATOR_HISTORY = (By.CLASS_NAME, "text text_type_digits-default")
    COMPLETED_ORDERS_COUNT = (By.XPATH, "//*[contains(text(),'Выполнено за все время')]/..//*[contains(@class,'Feed_number__')]")
    COMPLETED_ORDERS_COUNT_TODAY = (By.XPATH, "//*[contains(text(),'Выполнено за сегодня')]/..//*[contains(@class,'Feed_number__')]")
    IN_PROGRESS_ORDERS = (By.CSS_SELECTOR, "[class^='OrderFeed_orderListReady']")
