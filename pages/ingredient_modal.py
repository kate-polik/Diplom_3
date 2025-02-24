from pages.base_page import BasePage
from locators.ingredient_modal_locators import IngredientModalLocators


class IngredientModal(BasePage):

    def close_modal(self):
        """ Закрывает модальное окно кликом на крестик """
        self.find_element(IngredientModalLocators.CLOSE_BUTTON).click()


