from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        """Находит элемент на странице"""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def wait_for_text_in_element(self, locator, text, timeout=10):
        """Ожидает, пока в элементе появится определенный текст"""
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def click(self, locator):
        """Кликает на элемент"""
        self.find_element(locator).click()

    def is_element_visible(self, locator):
        """Проверяет, что элемент видим на странице"""
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_element_not_present(self, locator):
        """Проверяет, что элемент отсутствует на странице"""
        try:
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator))
            return True
        except:
            return False

    def get_current_url(self):
        """Возвращает текущий URL"""
        return self.driver.current_url

    def open_page(self, url):
        """Открывает страницу по указанному URL"""
        self.driver.get(url)

    def wait_for_text_to_change(self, locator, old_text, timeout=10):
        """Ожидает, пока текст элемента изменится с `old_text`"""
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.find_element(locator).text.strip() != old_text)
