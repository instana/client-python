# InfrastructureItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_health_info** | [**EntityHealthInfo**](EntityHealthInfo.md) |  | [optional] 
**label** | **str** |  | [optional] 
**metrics** | **Dict[str, List[List[float]]]** |  | [optional] 
**plugin** | **str** |  | [optional] 
**snapshot_id** | **str** |  | [optional] 
**tags** | **Dict[str, str]** |  | [optional] 
**time** | **int** | Epoch time in milliseconds if the snapshot is offline. Set to 9223372036854775807 if the snapshot is online. | [optional] 

## Example

```python
from instana_client.models.infrastructure_item import InfrastructureItem

# TODO update the JSON string below
json = "{}"
# create an instance of InfrastructureItem from a JSON string
infrastructure_item_instance = InfrastructureItem.from_json(json)
# print the JSON string representation of the object
print(InfrastructureItem.to_json())

# convert the object into a dict
infrastructure_item_dict = infrastructure_item_instance.to_dict()
# create an instance of InfrastructureItem from a dict
infrastructure_item_from_dict = InfrastructureItem.from_dict(infrastructure_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


