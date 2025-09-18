# PhysicalContext

The physical context of an entity. This is typically used to describe where a host, container or process fits into the infrastructure. 1. `cloudfoundry`: Contains physical context of Cloudfoundry. 2. `cluster`: Contains physical context of cluster like Hazelcast, Elasticsearch. 3. `container`: Contains physical context of container. 4. `host`: Contains physical context of host. 5. `kubernetes`: Contains physical context of Kubernetes. 6. `process`: Contains physical context of a process. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudfoundry** | [**CloudfoundryPhysicalContext**](CloudfoundryPhysicalContext.md) |  | [optional] 
**cluster** | [**SnapshotPreview**](SnapshotPreview.md) |  | [optional] 
**container** | [**SnapshotPreview**](SnapshotPreview.md) |  | [optional] 
**host** | [**SnapshotPreview**](SnapshotPreview.md) |  | [optional] 
**kubernetes** | [**KubernetesPhysicalContext**](KubernetesPhysicalContext.md) |  | [optional] 
**process** | [**SnapshotPreview**](SnapshotPreview.md) |  | [optional] 

## Example

```python
from instana_client.models.physical_context import PhysicalContext

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalContext from a JSON string
physical_context_instance = PhysicalContext.from_json(json)
# print the JSON string representation of the object
print(PhysicalContext.to_json())

# convert the object into a dict
physical_context_dict = physical_context_instance.to_dict()
# create an instance of PhysicalContext from a dict
physical_context_from_dict = PhysicalContext.from_dict(physical_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


