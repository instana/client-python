# UserBasicResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**full_name** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from instana_client.models.user_basic_result import UserBasicResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserBasicResult from a JSON string
user_basic_result_instance = UserBasicResult.from_json(json)
# print the JSON string representation of the object
print(UserBasicResult.to_json())

# convert the object into a dict
user_basic_result_dict = user_basic_result_instance.to_dict()
# create an instance of UserBasicResult from a dict
user_basic_result_from_dict = UserBasicResult.from_dict(user_basic_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


