install:
	uv sync

collectstatic:
	python manage.py collectstatic --noinput

migrate:
	python manage.py migrate

build:
	chmod +x ./build.sh
	./build.sh

render-start:
	gunicorn task_manager.wsgi --bind=0.0.0.0:8000