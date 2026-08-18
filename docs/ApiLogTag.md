# ApiLogTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from instana_client.models.api_log_tag import ApiLogTag

# TODO update the JSON string below
json = "{}"
# create an instance of ApiLogTag from a JSON string
api_log_tag_instance = ApiLogTag.from_json(json)
# print the JSON string representation of the object
print(ApiLogTag.to_json())

# convert the object into a dict
api_log_tag_dict = api_log_tag_instance.to_dict()
# create an instance of ApiLogTag from a dict
api_log_tag_from_dict = ApiLogTag.from_dict(api_log_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


