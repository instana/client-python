# LogsApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_time_frame** | **str** |  | [optional] 
**can_load_more** | **bool** |  | [optional] 
**items** | [**List[ApiLogItem]**](ApiLogItem.md) |  | [optional] 
**total_hits** | **int** |  | [optional] 

## Example

```python
from instana_client.models.logs_api_response import LogsApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LogsApiResponse from a JSON string
logs_api_response_instance = LogsApiResponse.from_json(json)
# print the JSON string representation of the object
print(LogsApiResponse.to_json())

# convert the object into a dict
logs_api_response_dict = logs_api_response_instance.to_dict()
# create an instance of LogsApiResponse from a dict
logs_api_response_from_dict = LogsApiResponse.from_dict(logs_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


