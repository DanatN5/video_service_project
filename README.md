# REST API сервис для работы с базой данных видео


## Установка и запуск:
1. Клонировать репозиторий
``` 
git clone git@github.com:DanatN5/video_service_project.git
```
````
cd video_service_project
````

2. Сконфигурируйте файл .env с со следущими переменными:

```
POSTGRES_PASSWORD=postgress
POSTGRES_USER=postgres
POSTGRES_DB=videos
DATABASE_URL=postgresql+asyncpg://postgres:postgress@db:5432/videos
```

3. Запуск через Docker Compose:
`````
make start_service
`````

4. Локальный запуск без Docker
`````
make install
`````
- Убедитесь что локальная БД Postgres настроена
`````
make runserver
`````

## Тестирование API с curl:

1. Создать видео
`````
curl -X POST "http://localhost:8000/videos" \
-H "Content-Type: application/json" \
-d '{
"video_path": "/storage/camera1/2024-01-15_10-30-00.mp4",
"start_time": "2024-01-15T10:30:00",
"duration": "PT1H",
"camera_number": 1,
"location": "Entrance"
}'
`````

2. Получить список видео с фильтрацией

`````
curl "http://localhost:8000/videos?
camera_number=1&camera_number=2&status=new&status=transcoded&location=Entra
nce&location=Exit"
`````

3. Обновить статус видео

`````
curl -X PATCH "http://localhost:8000/videos/1/status" \
-H "Content-Type: application/json" \
-d '{"status": "transcoded"}'
`````

4. Получить видео по ID

`````
curl "http://localhost:8000/videos/1"
`````
