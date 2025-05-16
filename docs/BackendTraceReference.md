# BackendTraceReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace_id** | **str** | The corresponding trace ID. For eg: &#x60;07eaf10c1d051234&#x60; or &#x60;000000000000000007eaf10c1d051234&#x60; | 

## Example

```python
from instana_client.models.backend_trace_reference import BackendTraceReference

# TODO update the JSON string below
json = "{}"
# create an instance of BackendTraceReference from a JSON string
backend_trace_reference_instance = BackendTraceReference.from_json(json)
# print the JSON string representation of the object
print(BackendTraceReference.to_json())

# convert the object into a dict
backend_trace_reference_dict = backend_trace_reference_instance.to_dict()
# create an instance of BackendTraceReference from a dict
backend_trace_reference_from_dict = BackendTraceReference.from_dict(backend_trace_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


