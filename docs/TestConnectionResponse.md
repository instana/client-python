# TestConnectionResponse

Response from a test connection request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected** | **bool** | Indicates whether the connection to the remote service was established successfully | 
**message** | **str** | A human-readable message describing the outcome of the connection test | 
**status_code** | **int** | The HTTP status code returned by the remote service during the connection test | 

## Example

```python
from instana_client.models.test_connection_response import TestConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestConnectionResponse from a JSON string
test_connection_response_instance = TestConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(TestConnectionResponse.to_json())

# convert the object into a dict
test_connection_response_dict = test_connection_response_instance.to_dict()
# create an instance of TestConnectionResponse from a dict
test_connection_response_from_dict = TestConnectionResponse.from_dict(test_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


