] Building 31.7s (10/12)                                                                                                  docker:default
 => [internal] load build definition from Dockerfile                                                                                  0.1s
 => => transferring dockerfile: 1.01kB                                                                                                0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                    0.6s
 => [auth] library/python:pull token for registry-1.docker.io                                                                         0.0s
 => [internal] load .dockerignore                                                                                                     0.0s
 => => transferring context: 2B                                                                                                       0.0s
 => [internal] load build context                                                                                                     0.1s
 => => transferring context: 2.21kB                                                                                                   0.0s
 => [1/7] FROM docker.io/library/python:3.9-slim@sha256:7a9cd42706c174cdcf578880ab9ae3b6551323a7ddbc2a89ad6e5b20a28fbfbe              0.0s
 => CACHED [2/7] WORKDIR /app                                                                                                         0.0s
 => CACHED [3/7] RUN apt-get update && apt-get install -y bash                                                                        0.0s
 => [4/7] RUN apt-get update && apt-get install -y wget gnupg &&     wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch   29.7s
 => ERROR [5/7] RUN wget -qO - https://repos.loki.dev/GPG-KEY-loki | apt-key add - &&     sh -c 'echo "deb https://repos.loki.dev/de  1.1s 
------
 > [5/7] RUN wget -qO - https://repos.loki.dev/GPG-KEY-loki | apt-key add - &&     sh -c 'echo "deb https://repos.loki.dev/deb stable main" > /etc/apt/sources.list.d/loki.list' &&     apt-get update && apt-get install -y loki:
0.535 Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
0.961 gpg: no valid OpenPGP data found.
------
Dockerfile:17
--------------------
  16 |     # Install Loki
  17 | >>> RUN wget -qO - https://repos.loki.dev/GPG-KEY-loki | apt-key add - && \
  18 | >>>     sh -c 'echo "deb https://repos.loki.dev/deb stable main" > /etc/apt/sources.list.d/loki.list' && \
  19 | >>>     apt-get update && apt-get install -y loki
  20 |     # Copy the application code
--------------------
ERROR: failed to solve: process "/bin/sh -c wget -qO - https://repos.loki.dev/GPG-KEY-loki | apt-key add - &&     sh -c 'echo \"deb https://repos.loki.dev/deb stable main\" > /etc/apt/sources.list.d/loki.list' &&     apt-get update && apt-get install -y loki" did not complete successfully: exit code: 2
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ 





The error you’re encountering is related to the use of `apt-key`, which has been deprecated in recent versions of Debian-based distributions. Additionally, it seems that the GPG key for the Loki repository cannot be retrieved correctly, leading to the `gpg: no valid OpenPGP data found` error.

To fix this issue, you can switch to using the new method of managing repository keys by placing the key in the `/etc/apt/trusted.gpg.d/` directory instead. Here’s how you can modify your Dockerfile:

### Updated Dockerfile Snippet

Replace the problematic section in your Dockerfile with the following:

```dockerfile
# Install Loki
RUN wget -qO - https://repos.loki.dev/GPG-KEY-loki | tee /etc/apt/trusted.gpg.d/loki.gpg > /dev/null && \
    echo "deb https://repos.loki.dev/deb stable main" > /etc/apt/sources.list.d/loki.list && \
    apt-get update && apt-get install -y loki
```

### Explanation
- **`tee /etc/apt/trusted.gpg.d/loki.gpg > /dev/null`**: This command retrieves the GPG key and saves it to the `trusted.gpg.d` directory, which is the new method of managing keys.
- **The rest of the command**: It remains the same, where it adds the Loki repository to the source list and then updates the package list and installs Loki.

### Full Dockerfile Context
Make sure that this updated snippet fits well into your existing Dockerfile, especially if there are any preceding lines that need to remain intact. Here’s how the full section might look:

```dockerfile
# Install dependencies
RUN apt-get update && apt-get install -y wget gnupg && \
    wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add - && \
    wget -qO - https://repos.loki.dev/GPG-KEY-loki | tee /etc/apt/trusted.gpg.d/loki.gpg > /dev/null && \
    echo "deb https://repos.loki.dev/deb stable main" > /etc/apt/sources.list.d/loki.list && \
    apt-get update && apt-get install -y loki
```

After making these changes, try rebuilding your Docker image. This should resolve the GPG key issue and allow the installation of Loki to proceed successfully.