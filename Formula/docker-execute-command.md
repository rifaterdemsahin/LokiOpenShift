The command you're looking for depends on whether you want to start a container interactively or execute a command in an already running container. Here’s how to use both approaches with `docker run` and `docker exec`:

### Start an Interactive Container
To start a container interactively, use `docker run` with the `-it` options:
```bash
docker run -it --name my-running-app my-image:latest
```
This opens an interactive terminal session where you can run commands within the container.

### Run a Container in Detached Mode
To run the container in the background (detached mode), use:
```bash
docker run -d --name my-running-app my-image:latest
```
This command starts the container and runs it in the background.

### Execute a Command in an Existing Running Container
To run a command in a container that’s already running, use `docker exec`:
```bash
docker exec -it my-running-app bash
```
This attaches you to a shell (`bash`) in the running container. You can replace `bash` with any other command you want to execute inside the container.