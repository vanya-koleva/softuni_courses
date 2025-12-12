# Commands

- Modified connection string:
```js
`mongodb://mongoadmin:secret@mongodb:27017/course-goals?authSource=admin`,
```

```bash
docker build -t serendipitysoftuni/goals-backend .

docker login

docker push serendipitysoftuni/goals-backend

docker volume create data

docker volume create logs

docker network create goals

# To create docker-compose.yml through https://www.composerize.com/
docker run -d --network goals --name mongodb \
    -v data:/data/db \
	-e MONGO_INITDB_ROOT_USERNAME=mongoadmin \
	-e MONGO_INITDB_ROOT_PASSWORD=secret \
	mongo
docker run -d -v logs:/logs --network goals --name backend -p 80:80 serendipitysoftuni/goals-backend
docker run -d --network goals --name frontend -p 3000:3000 serendipitysoftuni/goals-frontend

docker compose build

docker compose up -d
```

