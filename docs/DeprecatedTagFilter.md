# DeprecatedTagFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** |  | [optional] 
**name** | **str** |  | 
**operator** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from instana_client.models.deprecated_tag_filter import DeprecatedTagFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DeprecatedTagFilter from a JSON string
deprecated_tag_filter_instance = DeprecatedTagFilter.from_json(json)
# print the JSON string representation of the object
print(DeprecatedTagFilter.to_json())

# convert the object into a dict
deprecated_tag_filter_dict = deprecated_tag_filter_instance.to_dict()
# create an instance of DeprecatedTagFilter from a dict
deprecated_tag_filter_from_dict = DeprecatedTagFilter.from_dict(deprecated_tag_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


