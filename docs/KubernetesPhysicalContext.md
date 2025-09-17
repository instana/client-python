# KubernetesPhysicalContext

Contains physical context of Kubernetes which contains information about the cluster, namespace, node and pod.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**SnapshotPreview**](SnapshotPreview.md) |  | [optional] 
**namespace** | [**SnapshotPreview**](SnapshotPreview.md) |  | [optional] 
**node** | [**SnapshotPreview**](SnapshotPreview.md) |  | [optional] 
**pod** | [**SnapshotPreview**](SnapshotPreview.md) |  | [optional] 

## Example

```python
from instana_client.models.kubernetes_physical_context import KubernetesPhysicalContext

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesPhysicalContext from a JSON string
kubernetes_physical_context_instance = KubernetesPhysicalContext.from_json(json)
# print the JSON string representation of the object
print(KubernetesPhysicalContext.to_json())

# convert the object into a dict
kubernetes_physical_context_dict = kubernetes_physical_context_instance.to_dict()
# create an instance of KubernetesPhysicalContext from a dict
kubernetes_physical_context_from_dict = KubernetesPhysicalContext.from_dict(kubernetes_physical_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


