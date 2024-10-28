```markdown
# Creating Secrets in OpenShift

To create a secret in OpenShift, you can use the following command:

```sh
oc create secret generic logging-loki-s3 --type=s3
```

This command will create a secret with the name `logging-loki-s3` and type `s3`.

## Example

Here is an example of how to create the secret:

```sh
oc create secret generic logging-loki-s3 --type=s3
```

Make sure to replace any placeholders with your actual values.

For more information, refer to the [OpenShift documentation](https://docs.openshift.com/).
```