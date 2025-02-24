from selenium.webdriver.common.by import By


class AccountPageLocators:
    """Локаторы страницы личного кабинета"""
    ORDER_HISTORY_BUTTON = (By.XPATH,
                            "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")

    ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный кабинет")
    ORDER_HISTORY_TAB = (By.LINK_TEXT, "История заказов")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_NUMBERS_LOCATOR_ACCOUNT = (By.CLASS_NAME, "text text_type_digits-default")


