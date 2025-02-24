import requests
from constants import URLs
from constants import OrderData


class APIClient:
    @staticmethod
    def post(url, data, headers=None):
        return requests.post(url, json=data, headers=headers)

    @staticmethod
    def get(url, headers=None):
        return requests.get(url, headers=headers)

    @staticmethod
    def delete(url, headers=None):
        return requests.delete(url, headers=headers)

    @staticmethod
    def create_order(token, ingredients=None):
        """Создаёт заказ через API"""
        headers = {"Authorization": token, "Content-Type": "application/json"}

        # Используем переданные ингредиенты или список по умолчанию из констант
        data = {"ingredients": ingredients if ingredients else OrderData.DEFAULT_INGREDIENTS}

        response = requests.post(URLs.ORDERS, json=data, headers=headers)
        assert response.status_code == 200, f"Ошибка создания заказа: {response.text}"

        return response.json()  # Возвращаем JSON-ответ
