docker build . -t myelastic:latest


docker images

@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker images
REPOSITORY   TAG       IMAGE ID       CREATED             SIZE
myapp5       latest    a17907a24686   9 minutes ago       305MB
<none>       <none>    0d707167a879   13 minutes ago      305MB
myapp4       latest    2b860f455be1   15 minutes ago      286MB
myapp2       latest    858f3baae9c9   27 minutes ago      286MB
myapp3       latest    858f3baae9c9   27 minutes ago      286MB
<none>       <none>    73405b1892b6   31 minutes ago      286MB
<none>       <none>    85d438860b5e   35 minutes ago      286MB
my-image     latest    6c908a16227c   About an hour ago   286MB


docker run -it --name my-run-elastic myelastic:latest bash