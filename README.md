# Дипломный проект. Задание 3: Тестирование веб-приложения Stellar Burgers

## Структура проекта

Проект имеет следующую структуру:
```
Diplom_3
│── allure_results/           # Результаты Allure-отчётов
│── locators/                 # Локаторы элементов страниц
│── pages/                    # Реализация Page Object Model
│── tests/                    # Автоматизированные тесты
│── utils/                     # Вспомогательные утилиты
│── .gitignore                 # Исключения для Git
│── conftest.py                # Фикстуры Pytest
│── constants.py               # Константы проекта
│── README.md                  # Описание проекта
│── requirements.txt           # Зависимости проекта

```

## Описание проекта

В проекте тестируется веб-приложение **Stellar Burgers**. Для описания элементов, используемых в тестах, применён паттерн **Page Object Model (POM)**. Тестирование проводится в браузерах **Google Chrome** и **Mozilla Firefox**. Для формирования отчётов подключён **Allure**.

## Тесты

### Восстановление пароля (`test_password_recovery.py`)

- **Переход на страницу восстановления пароля по кнопке «Восстановить пароль»**  
  Тест: `test_navigate_to_password_recovery`

- **Ввод почты и клик по кнопке «Восстановить»**  
  Тест: `test_enter_email_and_submit_recovery`

- **Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его**  
  Тест: `test_toggle_password_visibility_activates_field`

### Личный кабинет (`test_account_section.py`)

- **Переход по клику на «Личный кабинет»**  
  Тест: `test_navigate_to_account`

- **Переход в раздел «История заказов»**  
  Тест: `test_navigate_to_order_history`

- **Выход из аккаунта**  
  Тест: `test_logout`

### Проверка основного функционала (`test_main_functionality.py`)

- **Переход по клику на «Конструктор»**  
  Тест: `test_navigate_to_constructor`

- **Переход по клику на «Лента заказов»**  
  Тест: `test_navigate_to_order_feed`

- **Если кликнуть на ингредиент, появится всплывающее окно с деталями**  
  Тест: `test_ingredient_modal`

- **Всплывающее окно закрывается кликом по крестику**  
  Тест: `test_close_ingredient_modal`

- **При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента**  
  Тест: `test_ingredient_counter_increases`

- **Залогиненный пользователь может оформить заказ**  
  Тест: `test_logged_in_user_can_place_order`

### Раздел «Лента заказов» (`test_order_feed.py`)

- **Если кликнуть на заказ, откроется всплывающее окно с деталями**  
  Тест: `test_order_feed`

- **Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»**  
  Тест: `test_orders_are_displayed_in_history_and_feed`

- **При создании нового заказа счётчик «Выполнено за всё время» увеличивается**  
  Тест: `test_completed_orders_counter_increases`

- **При создании нового заказа счётчик «Выполнено за сегодня» увеличивается**  
  Тест: `test_completed_orders_today_increases`

- **После оформления заказа его номер появляется в разделе «В работе»**  
  Тест: `test_order_number_appears_in_progress`

## Запуск тестов  
1. Установите зависимости:  
   ```sh
   pip3 install -r requirements.txt
    ```
2. Запустите тесты:  
   ```sh
    pytest tests --alluredir=allure_results
    ```
3. Сгенерируйте отчёт Allure::  
   ```sh
   allure serve allure_results  
    ```