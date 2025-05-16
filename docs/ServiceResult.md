# ServiceResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Service]**](Service.md) | Returns a list of Services. | [optional] 
**page** | **int** | Page number you want to retrieve in a request / retrieved in a response. | [optional] 
**page_size** | **int** | number of elements retrieved in a single query. | [optional] 
**total_hits** | **int** | The number of results returned. For eg: If &#x60;items&#x60; has 5 elements, &#x60;totalhits&#x60; will be 5 | [optional] 

## Example

```python
from instana_client.models.service_result import ServiceResult

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceResult from a JSON string
service_result_instance = ServiceResult.from_json(json)
# print the JSON string representation of the object
print(ServiceResult.to_json())

# convert the object into a dict
service_result_dict = service_result_instance.to_dict()
# create an instance of ServiceResult from a dict
service_result_from_dict = ServiceResult.from_dict(service_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


