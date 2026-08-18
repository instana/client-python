# AdvancedFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** |  | 
**metric** | [**EntityMetric**](EntityMetric.md) |  | 
**operator** | **str** |  | 
**threshold** | **float** |  | 

## Example

```python
from instana_client.models.advanced_filter import AdvancedFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedFilter from a JSON string
advanced_filter_instance = AdvancedFilter.from_json(json)
# print the JSON string representation of the object
print(AdvancedFilter.to_json())

# convert the object into a dict
advanced_filter_dict = advanced_filter_instance.to_dict()
# create an instance of AdvancedFilter from a dict
advanced_filter_from_dict = AdvancedFilter.from_dict(advanced_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


