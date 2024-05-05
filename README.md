1. Устанавливаем виртуальное окружение и зависимости
  1. python -m venv venv
  2. venv\Scripts\activate.bat
  3. pip install -r requirements.txt
2. Запускаем контейнер с бд PostgreSQL
  1. docker compose build
  2. docker compose up
3. Выполняем миграции БД python manage.py migrate
4. Запускаем проект python manage.py runserver
