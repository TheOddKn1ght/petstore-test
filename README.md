# Набор тестов Petstore API
Функциональный набор тестов для [Swagger Petstore API](https://petstore.swagger.io).

Используется:

* **Python 3**
* **pytest** — средство запуска тестов
* **requests** — HTTP-клиент
* **faker** — для генерации тестовых данных

##  Структура проекта
```
.
├── fixtures/                  # Фикстуры для генерации тестовых данных
│   ├── common_fixtures.py     # Общие фикстуры
│   └── negative_fixtures.py   # Фикстуры для негативных тестов
│
├── requirements.txt           # Список зависимостей проекта
│
├── tests/                     # Все тесты проекта
│   ├── conftest.py            # Конфигурация pytest
│   │
│   ├── pet/                   # Тесты для сущности "Pet"
│   │   ├── test_pet_crud.py       # Позитивные CRUD-тесты
│   │   └── test_pet_negative.py   # Негативные тесты
│   │
│   ├── store/                 # Тесты для сущности "Store"
│   │   ├── test_store_crud.py     # Позитивные CRUD-тесты заказов
│   │   └── test_store_negative.py # Негативные тесты для заказов
│   │
│   ├── user/                  # Тесты для сущности "User"
│   │   ├── test_user_crud.py      # CRUD-тесты для одного пользователя
│   │   ├── test_user_bulk_crud.py # Тесты для массового создания пользователей
│   │   └── test_user_negative.py  # Негативные тесты пользователей
│   │
│   └── resources/             # Вспомогательные ресурсы для тестов
│       └── images/            
│           └── test_pet.jpg   
│
└── utils/                     # Вспомогательные утилиты проекта
    └── api_client.py          # Wrapper для работы с API
```
