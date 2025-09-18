# ApiTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from instana_client.models.api_tag import ApiTag

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTag from a JSON string
api_tag_instance = ApiTag.from_json(json)
# print the JSON string representation of the object
print(ApiTag.to_json())

# convert the object into a dict
api_tag_dict = api_tag_instance.to_dict()
# create an instance of ApiTag from a dict
api_tag_from_dict = ApiTag.from_dict(api_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


