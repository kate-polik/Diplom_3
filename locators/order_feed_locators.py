from selenium.webdriver.common.by import By


class OrderFeedLocators:
    """Локаторы страницы 'Лента заказов''"""
    ORDER_FEED_HEADER = (By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-5']")
    FIRST_ORDER = (By.XPATH,
                   "//body/div[@id='root']/div[@class='App_App__aOmNj']/main[@class='App_componentContainer__2JC2W']/div[@class='OrderFeed_orderFeed__2RO_j']/div[@class='OrderFeed_contentBox__3-tWb']/ul[@class='OrderFeed_list__OLh59']/li[1]/a[1]")

    ORDER_DETAILS_MODAL = (
        By.XPATH, "//p[@class='text text_type_main-medium mb-8']")

    ORDER_NUMBERS_LOCATOR_HISTORY = (By.CLASS_NAME, "text text_type_digits-default")
    COMPLETED_ORDERS_COUNT = (By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]")
    COMPLETED_ORDERS_COUNT_TODAY = (By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")
    IN_PROGRESS_ORDERS = (By.CSS_SELECTOR, "[class^='OrderFeed_orderListReady']")
