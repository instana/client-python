# ApdexLevel

Apdex satisfaction level definition with threshold boundaries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the level | [optional] 
**lower** | **float** | Lower threshold boundary (inclusive) | [optional] 
**name** | **str** | Name of the satisfaction level | [optional] 
**upper** | **float** | Upper threshold boundary (inclusive) | [optional] 

## Example

```python
from instana_client.models.apdex_level import ApdexLevel

# TODO update the JSON string below
json = "{}"
# create an instance of ApdexLevel from a JSON string
apdex_level_instance = ApdexLevel.from_json(json)
# print the JSON string representation of the object
print(ApdexLevel.to_json())

# convert the object into a dict
apdex_level_dict = apdex_level_instance.to_dict()
# create an instance of ApdexLevel from a dict
apdex_level_from_dict = ApdexLevel.from_dict(apdex_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


