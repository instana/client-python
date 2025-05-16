# InfrastructureGroupsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_timeframe** | [**AdjustedTimeframe**](AdjustedTimeframe.md) |  | [optional] 
**can_load_more** | **bool** |  | [optional] 
**items** | [**List[InfrastructureGroup]**](InfrastructureGroup.md) |  | 
**next** | **object** | cursor to use between successive queries | [optional] 
**total_hits** | **int** | represents the total number of results | [optional] 

## Example

```python
from instana_client.models.infrastructure_groups_result import InfrastructureGroupsResult

# TODO update the JSON string below
json = "{}"
# create an instance of InfrastructureGroupsResult from a JSON string
infrastructure_groups_result_instance = InfrastructureGroupsResult.from_json(json)
# print the JSON string representation of the object
print(InfrastructureGroupsResult.to_json())

# convert the object into a dict
infrastructure_groups_result_dict = infrastructure_groups_result_instance.to_dict()
# create an instance of InfrastructureGroupsResult from a dict
infrastructure_groups_result_from_dict = InfrastructureGroupsResult.from_dict(infrastructure_groups_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


