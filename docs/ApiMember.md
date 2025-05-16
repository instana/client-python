# ApiMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from instana_client.models.api_member import ApiMember

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMember from a JSON string
api_member_instance = ApiMember.from_json(json)
# print the JSON string representation of the object
print(ApiMember.to_json())

# convert the object into a dict
api_member_dict = api_member_instance.to_dict()
# create an instance of ApiMember from a dict
api_member_from_dict = ApiMember.from_dict(api_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


