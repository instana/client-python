# ApdexEntity

Entity which holds the information of Apdex Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apdex_type** | **str** |  | 
**entity_id** | **str** |  | 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**threshold** | **int** |  | [optional] 

## Example

```python
from instana_client.models.apdex_entity import ApdexEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ApdexEntity from a JSON string
apdex_entity_instance = ApdexEntity.from_json(json)
# print the JSON string representation of the object
print(ApdexEntity.to_json())

# convert the object into a dict
apdex_entity_dict = apdex_entity_instance.to_dict()
# create an instance of ApdexEntity from a dict
apdex_entity_from_dict = ApdexEntity.from_dict(apdex_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


