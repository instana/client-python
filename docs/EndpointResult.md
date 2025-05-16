# EndpointResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Endpoint]**](Endpoint.md) | Returns a list of Endpoints. | [optional] 
**page** | **int** | Page number you want to retrieve in a request / retrieved in a response. | [optional] 
**page_size** | **int** | number of elements retrieved in a single query. | [optional] 
**total_hits** | **int** | The number of results returned. For eg: If &#x60;items&#x60; has 5 elements, &#x60;totalhits&#x60; will be 5 | [optional] 

## Example

```python
from instana_client.models.endpoint_result import EndpointResult

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointResult from a JSON string
endpoint_result_instance = EndpointResult.from_json(json)
# print the JSON string representation of the object
print(EndpointResult.to_json())

# convert the object into a dict
endpoint_result_dict = endpoint_result_instance.to_dict()
# create an instance of EndpointResult from a dict
endpoint_result_from_dict = EndpointResult.from_dict(endpoint_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


