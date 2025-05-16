# SloEntity

Entity of the Service Levels Objective Configuration, it could be either Application nor Website

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from instana_client.models.slo_entity import SloEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SloEntity from a JSON string
slo_entity_instance = SloEntity.from_json(json)
# print the JSON string representation of the object
print(SloEntity.to_json())

# convert the object into a dict
slo_entity_dict = slo_entity_instance.to_dict()
# create an instance of SloEntity from a dict
slo_entity_from_dict = SloEntity.from_dict(slo_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


