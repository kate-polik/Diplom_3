from pages.base_page import BasePage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators


class PasswordRecoveryPage(BasePage):

    def wait_for_password_recovery_header(self):
        """Ожидает появления заголовка 'Восстановление пароля'"""
        return self.find_element(PasswordRecoveryPageLocators.HEADER)

    def enter_email(self, email):
        self.enter_text(PasswordRecoveryPageLocators.EMAIL_INPUT, email)

    def click_recover(self):
        self.click(PasswordRecoveryPageLocators.RECOVER_BUTTON)

    def toggle_password_visibility(self):
        self.click(PasswordRecoveryPageLocators.TOGGLE_PASSWORD_VISIBILITY)

    def is_password_input_active(self):
        """Проверяет, что поле пароля стало активным"""
        return self.is_element_visible(PasswordRecoveryPageLocators.PASSWORD_INPUT_ACTIVE)
