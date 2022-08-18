# learning_log

python manage.py runserver - run app

### start project
1. Create django app - django-admin startproject learning_log
2. Create db, first migration - python manage.py migrate
3. python manage.py startapp learning_logs - create new app learning_logs
4. python manage.py createsuperuser - Создание суперпользователя

#### Work with apps
1. Создаем модель
2. Добавляем приложение в settings.py
3. Добавляем миграции - python manage.py makemigrations learning_logs
4. Сохраняем миграции - python manage.py migrate
5. Добавляем модель в админку - импортируем + admin.site.register(model)