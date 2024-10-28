PS C:\projects\LokiOpenShift> cd .\Symbols\
PS C:\projects\LokiOpenShift\Symbols> oc apply -f loki-stack.yaml
Error from server (NotFound): error when creating "loki-stack.yaml": namespaces "openshift-logging" not found
PS C:\projects\LokiOpenShift\Symbols> 


To resolve the error, you need to create the `openshift-logging` namespace before applying the `loki-stack.yaml` file. You can create the namespace using the following command:

```sh
oc create namespace openshift-logging
```

After creating the namespace, you can apply the `loki-stack.yaml` file again:

```sh
oc apply -f loki-stack.yaml
```


>>> operator install should ciover this¬!