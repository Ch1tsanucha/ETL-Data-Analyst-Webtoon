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
