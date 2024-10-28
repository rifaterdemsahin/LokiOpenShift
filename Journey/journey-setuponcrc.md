Setting up the loki in a crc environment for proof od concept
# Setup on CRC

## Logging into the Console

```sh
crc start
crc login
oc login --token=sha256~0WYm_orG0ewd9l9taqwXF6GE1feaRdPuk50DLkiAuG4 --server=https://api.crc.testing:6443
```

## Creating a New Project

```sh
oc new-project loki-operator
```


Create the storage class
Create the secrets

Go to the web interface and apply the operator

## Applying the LokiStack Configuration

🚀 Apply the LokiStack configuration:
```sh
oc apply -f lokistack.yaml
```

## Checking the LokiStack Status

🔍 Check the LokiStack status:
```sh
oc get lokistack -n loki-operator
```

## Getting the Pods in the Loki Operator Namespace

📦 Get the pods in the Loki operator namespace:
```sh
oc get pods -n loki-operator
```