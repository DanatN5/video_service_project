start_service:
	docker-compose up --build

runserver:
	uvicorn app.main:app --host localhost --port 8000 --reload
