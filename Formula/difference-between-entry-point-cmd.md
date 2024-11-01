# Difference Between ENTRYPOINT and CMD in Docker

When working with Docker, understanding the difference between `ENTRYPOINT` and `CMD` is crucial for defining the behavior of your containers. Both instructions are used to specify the command that should be run within a container, but they serve different purposes and have distinct behaviors.

## ENTRYPOINT

- **Purpose**: Sets the main command to be executed when the container starts.
- **Syntax**: 
    ```dockerfile
    ENTRYPOINT ["executable", "param1", "param2"]
    ```
- **Behavior**: 
    - The command defined in `ENTRYPOINT` will always be executed.
    - It is typically used to define the primary application of the container.
    - Arguments passed to `docker run` will be appended to the `ENTRYPOINT` command.

## CMD

- **Purpose**: Provides default arguments for the `ENTRYPOINT` command or specifies the command to run if `ENTRYPOINT` is not set.
- **Syntax**: 
    ```dockerfile
    CMD ["executable", "param1", "param2"]
    ```
- **Behavior**: 
    - If `ENTRYPOINT` is set, `CMD` provides default parameters for it.
    - If `ENTRYPOINT` is not set, `CMD` defines the command to be executed.
    - Arguments passed to `docker run` will override the `CMD` instruction.

## Examples

### Using ENTRYPOINT

```dockerfile
FROM ubuntu
ENTRYPOINT ["echo", "Hello"]
CMD ["World"]
```

- Running `docker run <image>` will output: `Hello World`
- Running `docker run <image> Docker` will output: `Hello Docker`

### Using CMD

```dockerfile
FROM ubuntu
CMD ["echo", "Hello World"]
```

- Running `docker run <image>` will output: `Hello World`
- Running `docker run <image> echo Goodbye` will output: `Goodbye`

## Summary

- Use `ENTRYPOINT` to define the main command that should always run.
- Use `CMD` to provide default arguments or a fallback command.
- Combining both allows for flexible and predictable container behavior.

Understanding these differences helps in creating more efficient and manageable Dockerfiles.
