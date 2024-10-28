oc new-project loki-operator

oc apply -f lokistack.yaml

oc get lokistack -n loki-operator

oc get pods -n loki-operator