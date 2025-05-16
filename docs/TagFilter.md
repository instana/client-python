# TagFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** | SOURCE or DESTINATION tag in case of a call tag. For Infrastructure, always set to NOT_APPLICABLE. | 
**key** | **str** | Tag key in case of a key/value tag. | [optional] 
**name** | **str** | Name of the tag. | 
**operator** | **str** |  | 
**value** | **object** | Tag value to filter on. Can be a string, number, or boolean value. | [optional] 

## Example

```python
from instana_client.models.tag_filter import TagFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TagFilter from a JSON string
tag_filter_instance = TagFilter.from_json(json)
# print the JSON string representation of the object
print(TagFilter.to_json())

# convert the object into a dict
tag_filter_dict = tag_filter_instance.to_dict()
# create an instance of TagFilter from a dict
tag_filter_from_dict = TagFilter.from_dict(tag_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


