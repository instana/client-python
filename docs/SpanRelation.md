# SpanRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**List[Application]**](Application.md) |  | 
**endpoint** | [**Endpoint**](Endpoint.md) |  | [optional] 
**physical_context** | [**PhysicalContext**](PhysicalContext.md) |  | [optional] 
**service** | [**Service**](Service.md) |  | [optional] 

## Example

```python
from instana_client.models.span_relation import SpanRelation

# TODO update the JSON string below
json = "{}"
# create an instance of SpanRelation from a JSON string
span_relation_instance = SpanRelation.from_json(json)
# print the JSON string representation of the object
print(SpanRelation.to_json())

# convert the object into a dict
span_relation_dict = span_relation_instance.to_dict()
# create an instance of SpanRelation from a dict
span_relation_from_dict = SpanRelation.from_dict(span_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


