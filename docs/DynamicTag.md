# DynamicTag

Structured dynamic tag prefixes with metadata 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | **List[str]** | List of prefix aliases | [optional] 
**can_apply_to_destination** | **bool** | Flag to identify if possible to apply for destination | [optional] 
**can_apply_to_source** | **bool** | Flag to identify if possible to apply for source | [optional] 
**category_labels** | **List[str]** | Category label | [optional] 
**icon** | **str** | Icon for the dynamic tag prefix | [optional] 
**prefix** | **str** | The actual prefix string | 
**type** | **str** | Type of the tag | [optional] 

## Example

```python
from instana_client.models.dynamic_tag import DynamicTag

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicTag from a JSON string
dynamic_tag_instance = DynamicTag.from_json(json)
# print the JSON string representation of the object
print(DynamicTag.to_json())

# convert the object into a dict
dynamic_tag_dict = dynamic_tag_instance.to_dict()
# create an instance of DynamicTag from a dict
dynamic_tag_from_dict = DynamicTag.from_dict(dynamic_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


