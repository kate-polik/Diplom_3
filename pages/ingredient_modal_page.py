from constants import URLs
from pages.base_page import BasePage
from locators.ingredient_modal_locators import IngredientModalLocators


class IngredientModal(BasePage):

    def close_modal(self):
        """ Закрывает модальное окно кликом на крестик """
        self.find_element(IngredientModalLocators.CLOSE_BUTTON).click()

    def is_ingredient_modal_closed(self):
        """Проверяет, что всплывающее окно ингредиента закрылось"""
        return self.is_element_not_present(IngredientModalLocators.INGREDIENT_MODAL_HEADER)

    def is_ingredient_modal_open(self):
        """Проверяет, открыт ли модальное окно с деталями ингредиента"""
        return self.get_current_url() == URLs.INGREDIENT_URL


