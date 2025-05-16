# GetCombinedMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | **List[str]** | Id of the exact metric you want to retrieve, eg. \&quot;cpu.user\&quot;, \&quot;clientrequests.read.mean\&quot; | 
**plugin** | **str** | Plugin name | 
**query** | **str** | Dynamic Focus Query | [optional] 
**rollup** | **int** | Rollup value in seconds | [optional] 
**snapshot_ids** | **List[str]** | Unique identifier the metrics are assigned to | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 

## Example

```python
from instana_client.models.get_combined_metrics import GetCombinedMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of GetCombinedMetrics from a JSON string
get_combined_metrics_instance = GetCombinedMetrics.from_json(json)
# print the JSON string representation of the object
print(GetCombinedMetrics.to_json())

# convert the object into a dict
get_combined_metrics_dict = get_combined_metrics_instance.to_dict()
# create an instance of GetCombinedMetrics from a dict
get_combined_metrics_from_dict = GetCombinedMetrics.from_dict(get_combined_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


