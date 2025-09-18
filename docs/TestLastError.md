# TestLastError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** |  | [optional] 
**start_time** | **int** |  | [optional] 

## Example

```python
from instana_client.models.test_last_error import TestLastError

# TODO update the JSON string below
json = "{}"
# create an instance of TestLastError from a JSON string
test_last_error_instance = TestLastError.from_json(json)
# print the JSON string representation of the object
print(TestLastError.to_json())

# convert the object into a dict
test_last_error_dict = test_last_error_instance.to_dict()
# create an instance of TestLastError from a dict
test_last_error_from_dict = TestLastError.from_dict(test_last_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


