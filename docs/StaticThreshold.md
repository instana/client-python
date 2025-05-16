# StaticThreshold

This threshold defines a static value to be evaluated with a specific operator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_updated** | **int** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from instana_client.models.static_threshold import StaticThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of StaticThreshold from a JSON string
static_threshold_instance = StaticThreshold.from_json(json)
# print the JSON string representation of the object
print(StaticThreshold.to_json())

# convert the object into a dict
static_threshold_dict = static_threshold_instance.to_dict()
# create an instance of StaticThreshold from a dict
static_threshold_from_dict = StaticThreshold.from_dict(static_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


