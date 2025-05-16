# CloudfoundryPhysicalContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**SnapshotPreview**](SnapshotPreview.md) |  | [optional] 
**cf_instance_index** | **str** |  | [optional] 
**organization** | [**SnapshotPreview**](SnapshotPreview.md) |  | [optional] 
**space** | [**SnapshotPreview**](SnapshotPreview.md) |  | [optional] 

## Example

```python
from instana_client.models.cloudfoundry_physical_context import CloudfoundryPhysicalContext

# TODO update the JSON string below
json = "{}"
# create an instance of CloudfoundryPhysicalContext from a JSON string
cloudfoundry_physical_context_instance = CloudfoundryPhysicalContext.from_json(json)
# print the JSON string representation of the object
print(CloudfoundryPhysicalContext.to_json())

# convert the object into a dict
cloudfoundry_physical_context_dict = cloudfoundry_physical_context_instance.to_dict()
# create an instance of CloudfoundryPhysicalContext from a dict
cloudfoundry_physical_context_from_dict = CloudfoundryPhysicalContext.from_dict(cloudfoundry_physical_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


