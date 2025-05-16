# PhysicalContext


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


