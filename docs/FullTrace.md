# FullTrace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**root_span** | [**Span**](Span.md) |  | 
**total_error_count** | **int** |  | [optional] 

## Example

```python
from instana_client.models.full_trace import FullTrace

# TODO update the JSON string below
json = "{}"
# create an instance of FullTrace from a JSON string
full_trace_instance = FullTrace.from_json(json)
# print the JSON string representation of the object
print(FullTrace.to_json())

# convert the object into a dict
full_trace_dict = full_trace_instance.to_dict()
# create an instance of FullTrace from a dict
full_trace_from_dict = FullTrace.from_dict(full_trace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


