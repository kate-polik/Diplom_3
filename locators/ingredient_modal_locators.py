from selenium.webdriver.common.by import By


class IngredientModalLocators:
    CLOSE_BUTTON = (By.XPATH,
                    "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//div[@class='Modal_modal__container__Wo2l_']//button[@type='button']//*//*")

    INGREDIENT_MODAL_HEADER = (By.XPATH,
                               "//h2[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10']")  # Заголовок всплывающего окна
