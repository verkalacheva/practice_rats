# Приложение для буккроссинга (Команда rats)
## Состав команды
- Калачева Вера Викторовна
- Крашенинникова Дарья Олеговна
- Таргович Наталья Павловна
- Денисов Илья Алексеевич
- Петрова Виктория Владимировна
- Марков Даниил Всеволодович
## Инструкция по запуску каждого модуля
1. cd practice_rats/{нужная папка}
2. pip install poetry 
3. poetry install
4. poetry run python manage.py makemigrations
5. poetry run python manage.py migrate
6. poetry run python manage.py runserver

Во всех модулях:
/swagger/ - путь к swagger

В модуле Users:

/users/login/ - login page

/users/register/ - registration page

