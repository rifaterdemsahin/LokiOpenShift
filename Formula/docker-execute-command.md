### Running Commands in Containers: Interactive Sessions with `docker run` and `docker exec`

The command you need depends on whether you're launching a new container interactively or executing a command in an already running container. Here’s how to use both `docker run` and `docker exec` for these tasks:

---

### Start an Interactive Container with `docker run`
To start a new container with an interactive terminal session, use the `-it` options:
```bash
docker run -it --name my-running-app3 myapp3:latest
```
This command starts a container and opens a terminal where you can run commands interactively within the container.

---

### Start a Detached Container
To run the container in the background (detached mode), add the `-d` option:
```bash
docker run -d --name my-running-app my-image:latest
```
This command launches the container in the background, allowing it to run without an attached terminal session.

---

### Run Commands in an Already Running Container with `docker exec`
To open a new shell or run commands in an existing container, use `docker exec` with the container name:
```bash
docker exec -it my-running-app bash
```
This command opens an interactive shell (`bash`) in the specified running container. Replace `bash` with any command you need to execute inside the container.

---

### Example with an Alternative Container Name
If you have another running container named `my-running-app7`:
```bash
docker exec -it my-running-app7 bash
```
This command opens an interactive `bash` session in `my-running-app7`. Ensure the container name is correct, as an error (`No such container`) will occur if the specified container isn’t found.

