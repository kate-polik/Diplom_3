from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Локаторы страницы логина"""
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH,
                    "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")

    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
