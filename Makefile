install:
	uv sync

collectstatic:
	uv run manage.py collectstatic --noinput

migrate:
	uv run manage.py migrate

build:
	chmod +x ./build.sh
	./build.sh

render-start:
	gunicorn task_manager.wsgi --bind=0.0.0.0:8000