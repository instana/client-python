# MetricItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** | Start of timeframe expressed as the Unix epoch time in milliseconds | [optional] 
**host** | **str** | Host name | [optional] 
**label** | **str** | Entitiy label | [optional] 
**metrics** | **Dict[str, List[List[float]]]** |  | [optional] 
**plugin** | **str** | Plugin name | [optional] 
**snapshot_id** | **str** | Id of the exact metric you want to retrieve, eg. \&quot;cpu.user\&quot;, \&quot;clientrequests.read.mean\&quot; | [optional] 
**tags** | **List[str]** | Entitiy tags | [optional] 
**to** | **int** | End of timeframe expressed as the Unix epoch time in milliseconds | [optional] 

## Example

```python
from instana_client.models.metric_item import MetricItem

# TODO update the JSON string below
json = "{}"
# create an instance of MetricItem from a JSON string
metric_item_instance = MetricItem.from_json(json)
# print the JSON string representation of the object
print(MetricItem.to_json())

# convert the object into a dict
metric_item_dict = metric_item_instance.to_dict()
# create an instance of MetricItem from a dict
metric_item_from_dict = MetricItem.from_dict(metric_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


