# Trace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** |  | [optional] 
**endpoint** | [**Endpoint**](Endpoint.md) |  | [optional] 
**erroneous** | **bool** |  | [optional] 
**id** | **str** |  | 
**label** | **str** |  | 
**service** | [**Service**](Service.md) |  | [optional] 
**start_time** | **int** |  | [optional] 

## Example

```python
from instana_client.models.trace import Trace

# TODO update the JSON string below
json = "{}"
# create an instance of Trace from a JSON string
trace_instance = Trace.from_json(json)
# print the JSON string representation of the object
print(Trace.to_json())

# convert the object into a dict
trace_dict = trace_instance.to_dict()
# create an instance of Trace from a dict
trace_from_dict = Trace.from_dict(trace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


