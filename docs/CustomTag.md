# CustomTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** | Aggregation to apply on the tag for every member. | [optional] 
**category** | **str** | Category of the tag in the catalog | [optional] 
**description** | **str** | Description to be used in the catalog | [optional] 
**label** | **str** | Label to be used in the catalog | [optional] 
**name** | **str** | Name of the tag. Will use the same value as the source tag if not specified. | [optional] 
**section** | **str** | Section of the tag in the catalog | [optional] 
**source** | **str** | Name of the source tag | [optional] 
**type** | **str** | Type of entity for the source tag | [optional] 

## Example

```python
from instana_client.models.custom_tag import CustomTag

# TODO update the JSON string below
json = "{}"
# create an instance of CustomTag from a JSON string
custom_tag_instance = CustomTag.from_json(json)
# print the JSON string representation of the object
print(CustomTag.to_json())

# convert the object into a dict
custom_tag_dict = custom_tag_instance.to_dict()
# create an instance of CustomTag from a dict
custom_tag_from_dict = CustomTag.from_dict(custom_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


