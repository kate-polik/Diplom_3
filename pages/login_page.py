from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def is_login_header_visible(self):
        """Проверяет, что заголовок 'Вход' отображается"""
        return self.is_element_visible(LoginPageLocators.LOGIN_HEADER)

    def enter_email(self, email):
        """Ввод email"""
        self.enter_text(LoginPageLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        """Ввод пароля"""
        self.enter_text(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        """Клик на кнопку 'Войти'"""
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def go_to_constructor(self):
        """Переход на страницу 'Конструктор'"""
        self.click(LoginPageLocators.CONSTRUCTOR_BUTTON)

    def go_to_password_recovery(self):
        """Кликает на кнопку 'Восстановить пароль'"""
        self.click(LoginPageLocators.RECOVER_PASSWORD_BUTTON)
