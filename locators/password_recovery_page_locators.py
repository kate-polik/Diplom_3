from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    HEADER = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")
    TOGGLE_PASSWORD_VISIBILITY = (By.XPATH, "//div[@class='input__icon input__icon-action']//*//*")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    PASSWORD_INPUT_ACTIVE = (By.XPATH,
                             '//div[@class="input__icon input__icon-action"]/ancestor::div[@class="input pr-6 pl-6 input_type_text input_size_default input_status_active"]')
