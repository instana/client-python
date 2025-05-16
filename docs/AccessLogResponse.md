# AccessLogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[AccessLogEntry]**](AccessLogEntry.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from instana_client.models.access_log_response import AccessLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessLogResponse from a JSON string
access_log_response_instance = AccessLogResponse.from_json(json)
# print the JSON string representation of the object
print(AccessLogResponse.to_json())

# convert the object into a dict
access_log_response_dict = access_log_response_instance.to_dict()
# create an instance of AccessLogResponse from a dict
access_log_response_from_dict = AccessLogResponse.from_dict(access_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


