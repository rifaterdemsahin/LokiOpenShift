@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker images
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
<none>       <none>    6c908a16227c   3 minutes ago   286MB
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $  docker build -t my-image:latest .
[+] Building 1.2s (10/10) FINISHED                                                                                                                                docker:default
 => [internal] load build definition from Dockerfile                                                                                                                        0.0s
 => => transferring dockerfile: 367B                                                                                                                                        0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                                                          0.6s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                               0.0s
 => [internal] load .dockerignore                                                                                                                                           0.1s
 => => transferring context: 2B                                                                                                                                             0.0s
 => [1/4] FROM docker.io/library/python:3.9-slim@sha256:7a9cd42706c174cdcf578880ab9ae3b6551323a7ddbc2a89ad6e5b20a28fbfbe                                                    0.0s
 => [internal] load build context                                                                                                                                           0.0s
 => => transferring context: 68B                                                                                                                                            0.0s
 => CACHED [2/4] WORKDIR /app                                                                                                                                               0.0s
 => CACHED [3/4] COPY . /app                                                                                                                                                0.0s
 => CACHED [4/4] RUN pip install --no-cache-dir -r requirements.txt                                                                                                         0.0s
 => exporting to image                                                                                                                                                      0.1s
 => => exporting layers                                                                                                                                                     0.0s
 => => writing image sha256:6c908a16227ce8af20e8592d7324ded67630c31f51f9f15b1593cc8e00f264bc                                                                                0.0s
 => => naming to docker.io/library/my-image:latest                                                                                                                          0.0s
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker images
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
my-image     latest    6c908a16227c   5 minutes ago   286MB
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ 


@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker run -d --name my-running-app my-image:latest
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker exec -it my-running-app /bin/bash

@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker start my-running-app
my-running-app
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker exec -it my-running-app /bin/bash

