@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker run -it --name my-run-elastic22 myelastic:latest bash
root@55076f054757:/app#    sysctl vm.max_map_count
vm.max_map_count = 65530
root@55076f054757:/app# sudo sysctl -w vm.max_map_count=262144
bash: sudo: command not found
root@55076f054757:/app# sysctl -w vm.max_map_count=262144
sysctl: permission denied on key "vm.max_map_count"
root@55076f054757:/app# sysctl -w vm.max_map_count=262144



The issue arises because Docker containers typically run with limited privileges, and certain system-level operations, like modifying kernel parameters, require elevated permissions. In this case, the `sysctl` command is being used to change the `vm.max_map_count` setting, which controls the maximum number of memory map areas a process may have.

To resolve this, you can run the Docker container with the `--privileged` flag, which grants the container extended privileges. Here is the updated command:

```sh
docker run -it --privileged --name my-run-elastic22 myelastic:latest bash
```

Alternatively, you can set the `vm.max_map_count` parameter on the host machine before starting the Docker container:

```sh
sudo sysctl -w vm.max_map_count=262144
```

This change will persist until the host machine is rebooted. To make it permanent, add the following line to `/etc/sysctl.conf`:

```sh
vm.max_map_count=262144
```

Then, apply the changes with:

```sh
sudo sysctl -p
```