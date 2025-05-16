# GetTraceDownloadResultItem

Represents an array of call group item containing several attributes that describe its properties. The item includes fields such as cursor, metrics, name, and timestamp, which provide detailed information about the item. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_count** | **int** | Number of calls in a trace. | [optional] 
**cursor** | **object** | Cursor to use between successive queries | [optional] 
**destination** | [**CallRelation**](CallRelation.md) |  | [optional] 
**duration** | **int** | The total time taken for the entire operation of a call, from the moment the request was initiated to when the response was received. The time measured is in milliseconds. This is also known as latency of a call. | [optional] 
**error_count** | **int** | Represents whether the call is erroneous or not. 0 is not erroneous and 1 is erroneous. | [optional] 
**foreign_parent_id** | **str** |  | [optional] 
**id** | **str** | The unique call id. For example: &#x60;1bcad5c82338deaf&#x60;. | [optional] 
**min_self_time** | **int** | The smallest self time in the batch. May be null to indicate that &#x60;minSelfTime&#x60; is unknown when this node has only an exit span and no children. The time measured is in milliseconds. | [optional] 
**name** | **str** | Name of the call. For example: &#x60;GET /articles/:id&#x60;. | [optional] 
**network_time** | **int** | exit span duration - entry span duration | [optional] 
**parent_id** | **str** | The parent call id, referring to another call in the same trace which triggered the processing associated with this call. | [optional] 
**timestamp** | **int** | The timestamp when the call or request was initiated. For example, Unix epoch time in milliseconds &#x60;1735532879870&#x60; is &#x60;Monday, 30 December 2024 04:27:59.870 GMT&#x60; | [optional] 

## Example

```python
from instana_client.models.get_trace_download_result_item import GetTraceDownloadResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetTraceDownloadResultItem from a JSON string
get_trace_download_result_item_instance = GetTraceDownloadResultItem.from_json(json)
# print the JSON string representation of the object
print(GetTraceDownloadResultItem.to_json())

# convert the object into a dict
get_trace_download_result_item_dict = get_trace_download_result_item_instance.to_dict()
# create an instance of GetTraceDownloadResultItem from a dict
get_trace_download_result_item_from_dict = GetTraceDownloadResultItem.from_dict(get_trace_download_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


