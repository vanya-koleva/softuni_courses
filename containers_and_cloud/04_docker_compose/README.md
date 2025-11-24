# Docker Compose and Container Orchestration

## Dockerfile

- The way to create custom images.

- Contains build instructions in a text file.

- Example:

```dockerfile
FROM node:16
ENV NODE_ENV=production
WORKDIR /app
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install --production
COPY . .
CMD [ "node", "server.js" ]
```

### Common Instructions

- `FROM` 
  
  - Base image to start from
  
  - Supports multi-staging
  
  - Each `FROM` starts a new stage

```dockerfile
FROM <image>

FROM <image>:<tag>

FROM <image>@<digest>
```

- `LABEL` – Add metadata

- `RUN` - Execute commands during build process

- `COPY`/`ADD` - Copy files from host to image

- `WORKDIR` - Set the working directory of the image, where your files are

- `EXPOSE` - Expose a port externaly

- `ENTRYPOINT` - Define the main command that starts the container

- `CMD` – Execute a command-line operation

- `VOLUME` – Define a volume for the container

- `ENV` – Set environment variables

### Commands

```bash
# Build an image
docker build [OPTIONS] PATH | URL | -

# List images
docker images

# Run a container from the image
docker run –d image

# Login to Docker Hub
docker login

# Push to Docker Hub
docker push {username}/{app}
```
