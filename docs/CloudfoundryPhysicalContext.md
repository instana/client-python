# CloudfoundryPhysicalContext

Contains physical context of Cloudfoundry. It contains the following information: 1. `application`: Application running within Cloud Foundry environment. 2. `cfInstanceIndex`: A unique ID of the container created and managed by Garden in the Cloud Foundry environment. 3. `organization`: Organization in the Cloud Foundry environment. 4. `space`: Space within an organization in Cloud Foundry environment. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**SnapshotPreview**](SnapshotPreview.md) |  | [optional] 
**cf_instance_index** | **str** | A unique ID of the container created and managed by Garden in the Cloud Foundry environment. | [optional] 
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


