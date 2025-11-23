# Containers and Docker

## Definitions

- **Containerization** - A method of packaging applications and their dependencies so they run consistently across different environments.

- **Image** - A lightweight, read-only template that contains everything needed to create a container (code, runtime, libraries, settings).

- **Container** - A running instance of an image; an isolated environment where the application executes.

- **Docker** - Containerization platform.

## VMs vs Containers

- **Virtual Machines:**
  
  - Virtualize the hardware
  
  - Complete isolation
  
  - Complete OS instalation
  
  - Heavier, slower to start, and use more resources.

- **Containers**
  
  - Virtualize the OS
  
  - Isolation is lighter
  
  - Share the host OS kernel
  
  - Lightweight, fast to start, and use fewer resources

## Containerization – Advantages

- **Portability** - “Build once, run anywhere” across different environments. Depends on container runtime and can run on any machine that supports it.

- **Consistency** - Eliminates “works on my machine” issues by packaging all dependencies.

- **Immutability** - Once a container is created, it doesn't change.

- **Efficient resource usage**  - Share the same OS kernel.

- **Isolation** - Applications run in separate, isolated environments.

- **Scalability** - Easy to scaled up or down.

## Docker

### Image

- A read-only blueprint ("recipe") for a container.

- If you want to change anything inside it, you build a new image

- It defines everything the container needs: base OS layer, frameworks, dependencies, configuration, and application code.

### Container

- A running instance of a Docker image.

- It is lightweight, isolated and secured.

- You can start, stop, move, or delete containers without affecting the image.

- Different app components may reside in separate containers.

### Docker Hub

- A cloud-based registry where you can find, store, and share Docker images.

- Supports public and private repositories.

- Automated builds and webhooks.

### Docker Compose

- A tool for defining and running multi-container applications.
  
  - e.g., WordPress requires Linux + NGINX + PHP + MySQL
  
  - Each component may run in a separate Docker container

### Docker CLI

- The command-line interface for interacting with Docker.

- Allows you to build, run, stop, and manage containers and images using commands.

```bash
docker pull [image]

docker run [image]

docker images

docker ps

docker logs [container]

docker start [container]

docker stop [container]

docker rm [container]

docker rmi [image]

# Open a shell inside a running container
docker exec -it [container] /bin/sh

docker inspect [container]

docker top [container]
```

### Common Command Flags

```bash
# Basic structure
docker run [FLAGS] IMAGE [COMMAND]
```

- **`-d`** or **`--detach`**
  
  - Run container in background (detached mode)
  
  - Returns control to terminal immediately

- **`-it`** 
  
  - **`-i`** = Keep STDIN open (interactive)
  
  - **`-t`** = Allocate a pseudo-TTY (terminal)
  
  - Combined: Creates an interactive shell session

- **`--rm`**
  
  - Automatically remove container when it exits
  
  - Useful for temporary/testing containers

- **`-p`** or **`--publish`**
  
  - Map container port to host port
  
  - Format: `-p HOST_PORT:CONTAINER_PORT`
  
```bash
docker run -p 8080:80 nginx    # Host:8080 → Container:80
```

- **`-P`** or **`--publish-all`**
  
  - Publish all exposed ports to random host ports

- **`-e`** or **`--env`**
  
  - Set environment variables inside container

- **`--env-file`**
  
  - Load environment variables from file

- **`--name`**
  
  - Assign custom name to container (instead of random)

- **`-v`** or **`--volume`**
  
  - Mount volumes/bind mounts

- **`-w`** or **`--workdir`**
  
  - Sets the working directory inside the container
  
  - The command will execute from this directory

## Data in Docker Containers

### Layered File System

- Each image has file system layers, which are read-only and isolated.

- Each layer represents a set of filesystem changes (like adding files or installing packages).

- Layers are stacked on top of each other to form the final image.

- Common layers can be shared across images.

### Container Isolation

- Each container is isolated and has its own writable file system.

- By default, data inside a container is ephemeral - it disappears when the container is removed.

### Volumes

- Special type of directory on the host. Stored by default in `/var/lib/docker/volumes/` on the host (Linux)

- Managed by Docker

- Data persists even after the container is deleted

- Image updates won't affect volumes

- Can be shared and reused among containers

### Bind Mounts

- Links a file or directory from the host machine directly into a Docker container.

- Changes made on the host or inside the container reflect immediately on the other side.

- Files are stored on host in your specified location.

- Docker does not manage the storage - it relies on the host filesystem.

- Potential security issue - container has broad access to user data

### Commands

- **Volumes**

```bash
# Create a volume
docker volume create my_volume

# List volumes
docker volume ls

# Inspect a volume
docker volume inspect my_volume

# Remove a volume (must not be in use)
docker volume rm my_volume

# Remove unused volumes
docker volume prune

# Mount volume to container
docker run -d --name myapp -v my_volume:/app/data nginx
```

- **Bind Mounts**

```bash
# Absolute path
docker run -d --name myapp -v /home/user/app/data:/app/data nginx

# Read-only bind mount
docker run -d --name myapp -v /home/user/app/data:/app/data:ro nginx
```

- **Mixed Approach**

```bash
# Volume for data, bind mount for config
docker run -p 5001:80 -d \
  -v app_data:/app/data \
  -v $(pwd)/config:/app/config:ro \
  nginxdemos/hello
```

- **Comparison**

| Command | Type | Data Location | Use Case |
|---------|------|---------------|----------|
| `-v app_data:/app/data` | **Volume** | `/var/lib/docker/volumes/` | App data, databases |
| `-v $(pwd)/src:/app/src` | **Bind Mount** | Host current directory | Source code, development |
