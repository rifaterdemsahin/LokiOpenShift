```markdown
# Creating Secrets in OpenShift

To create a secret in OpenShift, you can use the following command:

PS C:\projects\LokiOpenShift> oc login --token=sha256~PY9hzyyqqzc2MaM9igfL9OuAfPuLKoFXSUyGjkRT2cU --server=https://api.crc.testing:6443
Logged into "https://api.crc.testing:6443" as "kubeadmin" using the token provided.

You have access to 66 projects, the list has been suppressed. You can list all projects with 'oc projects'

Using project "loki-operator".
PS C:\projects\LokiOpenShift> 



```sh
oc create secret generic logging-loki-s3 --type=s3
```

This command will create a secret with the name `logging-loki-s3` and type `s3`.

PS C:\projects\LokiOpenShift> oc create secret generic logging-loki-s3 --type=s3
secret/logging-loki-s3 created
PS C:\projects\LokiOpenShift> 


## Example

Here is an example of how to create the secret:

```sh
oc create secret generic logging-loki-s3 --type=s3
```

Make sure to replace any placeholders with your actual values.

For more information, refer to the [OpenShift documentation](https://docs.openshift.com/).
```