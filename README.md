1. Устанавливаем виртуальное окружение и зависимости
   + python -m venv venv
   + venv\Scripts\activate.bat
   + pip install -r requirements.txt
2. Запускаем контейнер с бд PostgreSQL
   - docker compose build
   - docker compose up
3. Выполняем миграции БД python manage.py migrate
4. Запускаем проект python manage.py runserver
