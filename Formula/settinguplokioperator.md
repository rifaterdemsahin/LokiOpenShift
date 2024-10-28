# Setting Up Loki Operator in an OpenShift Cluster

Follow these steps to set up the Loki Operator in your OpenShift cluster:

## Prerequisites
- OpenShift CLI (`oc`) installed and configured
- Admin access to the OpenShift cluster

## Step 1: Create a New Project
```sh
oc new-project loki-operator
```

## Step 2: Install the Operator Lifecycle Manager (OLM)
If OLM is not already installed, follow the instructions [here](https://github.com/operator-framework/operator-lifecycle-manager).

## Step 3: Install the Loki Operator
1. Go to the OpenShift Web Console.
2. Navigate to **Operators** > **OperatorHub**.
3. Search for "Loki Operator".
4. Click on the Loki Operator and then click **Install**.
5. Follow the prompts to install the operator in the `loki-operator` namespace.

## Step 4: Create a LokiStack Custom Resource
Create a file named `lokistack.yaml` with the following content:
```yaml
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
    name: lokistack-sample
    namespace: loki-operator
spec:
    size: 1x.small
    storage:
        schemas:
            - version: v11
                effectiveDate: "2020-10-24"
        secret:
            name: loki-storage-secret
```

Apply the custom resource:
```sh
oc apply -f lokistack.yaml
```

## Step 5: Verify the Installation
Check the status of the LokiStack:
```sh
oc get lokistack -n loki-operator
```

Ensure all pods are running:
```sh
oc get pods -n loki-operator
```

## Conclusion
You have successfully set up the Loki Operator in your OpenShift cluster. You can now use Loki for log aggregation and monitoring.
