# Cluster Log Forwarder

Create by completing the form. Default values may be provided by the Operator authors.

## Configure via:

- **Form view**
- **YAML view**

## Cluster Log Forwarder

Provided by Red Hat

> **Note:** Some fields may not be represented in this form view. Please select "YAML view" for full control.

### Name
`logging`

### Labels
`app=frontend`

## Log Forwarder Outputs

Outputs are named destinations for log messages.

## Log Forwarder Pipelines

Pipelines forward the messages selected by a set of inputs to a set of outputs.

### Output Name
`default-output`

### Default Log Forwarder Pipeline

The default pipeline configuration forwards all logs to the default output.

```yaml
apiVersion: "logging.openshift.io/v1"
kind: "ClusterLogForwarder"
metadata:
    name: "instance"
spec:
    pipelines:
        - name: "default-pipeline"
            inputRefs:
                - "application"
                - "infrastructure"
                - "audit"
            outputRefs:
                - "default-output"
```


### OutputRefs

The `outputRefs` field lists the names (`output.name`) of outputs from this pipeline. These outputs define where the log messages will be sent.

```yaml
spec:
    outputs:
        - name: "default-output"
          type: "elasticsearch"
          url: "https://es.example.com:9200"
```


### Service Account

The default service account name used by the log forwarder is `log-forwarder-sa`.


>>>> if they are missing go ahead and create 