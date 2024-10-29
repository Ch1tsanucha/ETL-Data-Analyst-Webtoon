-- run start_airflow.sh to start make airflow service --

-- Add Proxy --
  docker-socket-proxy:
    image: tecnativa/docker-socket-proxy:latest
    restart: always
    environment:
      CONTAINERS: 1
      IMAGES: 1
      AUTH: 1
      POST: 1
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
-- to make airflow can run docker image --

-- Make webtoon Database for postgres --
psql -h <DB_HOST> -U <DB_USER> -d <DB_NAME> -p <DB_PORT>
example
docker exec -it <docker id of postgres> psql -h postgres -U airflow -d airflow -p 5432
-h HOST
-U USER
-d DATABASE_NAME
-p PORT
--------------------------------------------


