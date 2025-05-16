# TagMatcherDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** |  | 
**key** | **str** |  | 
**operator** | **str** |  | 
**value** | **str** |  | [optional] 

## Example

```python
from instana_client.models.tag_matcher_dto import TagMatcherDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TagMatcherDTO from a JSON string
tag_matcher_dto_instance = TagMatcherDTO.from_json(json)
# print the JSON string representation of the object
print(TagMatcherDTO.to_json())

# convert the object into a dict
tag_matcher_dto_dict = tag_matcher_dto_instance.to_dict()
# create an instance of TagMatcherDTO from a dict
tag_matcher_dto_from_dict = TagMatcherDTO.from_dict(tag_matcher_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


