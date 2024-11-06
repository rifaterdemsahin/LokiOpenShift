@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker run -it --privileged --name my-run-elastic222 myelastic:latest bash
root@fa2210a66723:/app# ```sh
> sudo sysctl -w vm.max_map_count=262144
> service elasticsearch start
> top
> 
> 
> htop
> 
> ^C
root@fa2210a66723:/app# sysctl -w vm.max_map_count=262144
vm.max_map_count = 262144
root@fa2210a66723:/app# service elasticsearch start
Starting Elasticsearch Server: failed!
root@fa2210a66723:/app# 