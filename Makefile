wsgi:
	poetry run python manage.py runserver

asgi:
	poetry run python -m web_api.asgi

migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

lint:
	poetry run black .

local:
	touch web_api/config/local.py
