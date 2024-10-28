oc new-project loki-operator
```markdown
🚀 Apply the LokiStack configuration:
```sh
oc apply -f lokistack.yaml
```

🔍 Check the LokiStack status:
```sh
oc get lokistack -n loki-operator
```

📦 Get the pods in the Loki operator namespace:
```sh
oc get pods -n loki-operator
```
```