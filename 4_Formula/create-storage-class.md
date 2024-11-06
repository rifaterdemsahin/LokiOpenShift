# Creating a Storage Class in OpenShift

A Storage Class in OpenShift allows you to define different types of storage and their properties. Here’s how you can create one:

## Prerequisites

- OpenShift cluster up and running
- Administrative access to the cluster

## Steps

1. **Create a YAML file for the Storage Class:**

    ```yaml
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: my-storage-class
    provisioner: kubernetes.io/aws-ebs
    parameters:
      type: gp2
      fsType: ext4
    ```

2. **Apply the YAML file to create the Storage Class:**

    ```sh
    oc apply -f my-storage-class.yaml
    ```

    PS C:\projects\LokiOpenShift\Symbols> oc apply -f my-storage-class.yaml
storageclass.storage.k8s.io/my-storage-class created
PS C:\projects\LokiOpenShift\Symbols>

3. **Verify the Storage Class:**

    ```sh
    oc get storageclass
    ```

## Example

Here is an example of creating a Storage Class for AWS EBS:

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: aws-ebs-sc
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
  fsType: ext4
```

Apply the configuration:

```sh
oc apply -f aws-ebs-sc.yaml
```

Verify the creation:

```sh
oc get storageclass
```

## Conclusion

You have successfully created a Storage Class in OpenShift. You can now use this Storage Class to dynamically provision storage for your applications.
