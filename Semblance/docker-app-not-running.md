Error response from daemon: container 2cec247007263d3d17f7c9959deaed6b1ee0c578627cbb831093e2ad3eb3bab4 is not running
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker start my-running-app
my-running-app
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker exec -it my-running-app /bin/bash
Error response from daemon: container 2cec247007263d3d17f7c9959deaed6b1ee0c578627cbb831093e2ad3eb3bab4 is not running
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker images
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
my-image     latest    6c908a16227c   19 minutes ago   286MB
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker ps -A
unknown shorthand flag: 'A' in -A
See 'docker ps --help'.
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker ps -a
CONTAINER ID   IMAGE             COMMAND            CREATED              STATUS                      PORTS     NAMES
2cec24700726   my-image:latest   "python main.py"   About a minute ago   Exited (2) 25 seconds ago             my-running-app
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ 