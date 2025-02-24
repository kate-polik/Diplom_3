from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы"""

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    MAIN_HEADER = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    SECOND_INGREDIENT = (By.XPATH,
                         "//body/div[@id='root']/div[@class='App_App__aOmNj']/main[@class='App_componentContainer__2JC2W']/section[@class='BurgerIngredients_ingredients__1N8v2']/div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[1]/a[2]/img[1]")

    INGREDIENT_COUNTER = (
        By.XPATH, "//p[@class='counter_counter__num__3nue1'][contains(text(),'2')]")  # Счетчик ингредиента

    ORDER_CONFIRMATION_HEADER = (By.XPATH,
                                 "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")

    ORDER_CONSTRUCTOR = (By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[@type='button']")
