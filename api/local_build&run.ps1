docker stop bdm_api
docker rm bdm_api
docker rmi bdm_api

docker build -t bdm_api .
docker run --env-file app/.env -e PORT=80 -d --name bdm_api -p 80:80 bdm_api

start http://localhost/docs

pause