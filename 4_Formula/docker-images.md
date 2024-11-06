@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker images
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
<none>       <none>    6c908a16227c   3 minutes ago   286MB
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ 


```bash
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker build -t my-image:latest .
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM alpine
 ---> a24bb4013296
Step 2/4 : COPY . /app
 ---> Using cache
 ---> 0a1b2c3d4e5f
Step 3/4 : RUN apk add --no-cache python3 py3-pip
 ---> Using cache
 ---> 1a2b3c4d5e6f
Step 4/4 : CMD ["python3", "/app/my_script.py"]
 ---> Using cache
 ---> 2b3c4d5e6f7g
Successfully built 3c4d5e6f7g8h
Successfully tagged my-image:latest
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker images
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
my-image     latest    3c4d5e6f7g8h   10 seconds ago   5.6MB
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $
```

@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker images
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
my-image     latest    6c908a16227c   5 minutes ago   286MB
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ 