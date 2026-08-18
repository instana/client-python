# EntityMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Entity Metric | 
**scope** | [**EntityMetricScope**](EntityMetricScope.md) |  | [optional] 

## Example

```python
from instana_client.models.entity_metric import EntityMetric

# TODO update the JSON string below
json = "{}"
# create an instance of EntityMetric from a JSON string
entity_metric_instance = EntityMetric.from_json(json)
# print the JSON string representation of the object
print(EntityMetric.to_json())

# convert the object into a dict
entity_metric_dict = entity_metric_instance.to_dict()
# create an instance of EntityMetric from a dict
entity_metric_from_dict = EntityMetric.from_dict(entity_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


