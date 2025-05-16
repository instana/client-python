# InfrastructureGroup

group of infrastructure entities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | number of entities in this group | [optional] 
**metrics** | **Dict[str, List[List[float]]]** | map of metric keys to array of timestamp,value pairs | [optional] 
**tags** | **Dict[str, object]** | tag keys and values for this group | [optional] 

## Example

```python
from instana_client.models.infrastructure_group import InfrastructureGroup

# TODO update the JSON string below
json = "{}"
# create an instance of InfrastructureGroup from a JSON string
infrastructure_group_instance = InfrastructureGroup.from_json(json)
# print the JSON string representation of the object
print(InfrastructureGroup.to_json())

# convert the object into a dict
infrastructure_group_dict = infrastructure_group_instance.to_dict()
# create an instance of InfrastructureGroup from a dict
infrastructure_group_from_dict = InfrastructureGroup.from_dict(infrastructure_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


