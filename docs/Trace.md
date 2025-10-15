# Trace

1. `service`: The service from where trace started. 2. `endpoint`: Endpoint of the service. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | Total time taken for a trace to finish. | [optional] 
**endpoint** | [**Endpoint**](Endpoint.md) |  | [optional] 
**erroneous** | **bool** | Flag which tells whether the trace is erroneous or not | [optional] 
**id** | **str** | The trace ID. All spans of the same trace must have the same trace ID. For example, &#x60;e93282c0d5018320&#x60;. | 
**label** | **str** | Name of the trace. | 
**service** | [**Service**](Service.md) |  | [optional] 
**start_time** | **int** | The start time of the trace. | [optional] 

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


