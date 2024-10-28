# Starting CRC with 16 GB of Memory in OpenShift

To start CodeReady Containers (CRC) with 16 GB of memory in OpenShift, follow these steps:

1. **Stop CRC if it's running:**
    ```sh
    crc stop
    crc delete >>> nuke it
    ```

2. **Configure CRC to use 16 GB of memory:**
    ```sh
    crc config set memory 16384
    ```

3. **Start CRC:**
    ```sh
    crc start
    ```

This will allocate 16 GB of memory to your CRC instance.
