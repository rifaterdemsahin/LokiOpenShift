```mermaid
graph TD
    A[Start CRC] --> B[Login to CRC Console]
    B --> C[Login to OpenShift]
    
    C -->|Install| D[Loki Operator]
    D --> E[Create New Project: loki-operator]
    E --> F[Create Storage Class and Secrets]
    
    F --> G[Apply LokiStack Configuration]
    G --> H[Check LokiStack Status]
    H --> I[Get Pods in Loki Operator Namespace]

