# EntityMetricScope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**type** | **str** | Type of the Entity Metric. Eg. For Mobile App SLO it would be any of the supported beaconTypes | 

## Example

```python
from instana_client.models.entity_metric_scope import EntityMetricScope

# TODO update the JSON string below
json = "{}"
# create an instance of EntityMetricScope from a JSON string
entity_metric_scope_instance = EntityMetricScope.from_json(json)
# print the JSON string representation of the object
print(EntityMetricScope.to_json())

# convert the object into a dict
entity_metric_scope_dict = entity_metric_scope_instance.to_dict()
# create an instance of EntityMetricScope from a dict
entity_metric_scope_from_dict = EntityMetricScope.from_dict(entity_metric_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


