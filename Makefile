start_bd:
	docker-compose up -d

shut_down_bd:
	docker-compose down

_venv:
	source venv/bin/activate


runserver:
	uvicorn app.main:app --host localhost --port 8000 --reload
