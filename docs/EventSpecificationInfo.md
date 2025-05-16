# EventSpecificationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**entity_type** | **str** |  | 
**id** | **str** |  | 
**invalid** | **bool** |  | [optional] 
**migrated** | **bool** |  | [optional] 
**name** | **str** |  | 
**severity** | **int** |  | [optional] 
**triggering** | **bool** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from instana_client.models.event_specification_info import EventSpecificationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EventSpecificationInfo from a JSON string
event_specification_info_instance = EventSpecificationInfo.from_json(json)
# print the JSON string representation of the object
print(EventSpecificationInfo.to_json())

# convert the object into a dict
event_specification_info_dict = event_specification_info_instance.to_dict()
# create an instance of EventSpecificationInfo from a dict
event_specification_info_from_dict = EventSpecificationInfo.from_dict(event_specification_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


