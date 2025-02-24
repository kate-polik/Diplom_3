class URLs:
    """Константы для URL-адресов"""
    BASE_URL = "https://stellarburgers.nomoreparties.site/"
    ORDER_HISTORY = BASE_URL + "account/order-history"
    LOGIN_PAGE = BASE_URL + "login"
    INGREDIENT_URL = BASE_URL + "ingredient/61c0c5a71d1f82001bdaaa6c"  # URL страницы ингредиента

    # API эндпоинты
    REGISTER = BASE_URL + "api/auth/register"
    USER = BASE_URL + "api/auth/user"
    LOGIN = BASE_URL + "api/auth/login"
    ORDERS = BASE_URL + "api/orders"


class TestUserData:
    """Тестовые данные для пользователей"""
    TEST_EMAIL = "test@example.com"


class OrderData:
    """Константы для тестовых данных заказов"""
    DEFAULT_INGREDIENTS = [
        "61c0c5a71d1f82001bdaaa7a",
        "61c0c5a71d1f82001bdaaa6f",
        "61c0c5a71d1f82001bdaaa77",
        "61c0c5a71d1f82001bdaaa79",
    ]
