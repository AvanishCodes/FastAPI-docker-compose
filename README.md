# Docker Compose for a FastAPI application

Build the docker image for the application

- `docker build -t fastapi-image .`.

Check if the image is built

- `docker images`.

Run the docker container

- `docker run --name fastapi-container -p 80:80 fastapi-image`.

Remove the container

- `docker rm fastapi-container`.

Run the docker container in detached mode

- `docker run --name fastapi-container -p 80:80 -d fastapi-image`.

Check if the container is running

- `docker ps`.

However, the changes we've made here will not be reflected to the container even though we've used the live reload in fastAPI.

We need to create a mapping that helps us to reflect the changes in the container.

First, delete both image and the container.

- `docker stop fastapi-container`.

- `docker rm fastapi-container`.

Here comes the role of [docker volumes](https://docs.docker.com/storage/volumes/).

Run the container on a volume

- `docker run --name fastapi-container -p 80:80 -v $(pwd):/code -d fastapi-image`.

Now, the changes we'll make to the docker container will be reflected live in the container.

For VS Code only

- Use Remote Window(in bottom left) -> Attach a running container. Now open your folder inside the container.

- Any change you will make in your local shal be instantly reflected to the container.

Write the `docker-compose.yml` file.

Now, run the command `docker-compose up` to run the container.

To stop the container, run `docker-compose down`.
