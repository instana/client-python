# CallGroupsItem

Represents an array of call group item containing several attributes that describe its properties. The item includes fields such as cursor, metrics, name, and timestamp, which provide detailed information about the item. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **object** | Cursor to use between successive queries | 
**metrics** | **Dict[str, List[List[float]]]** | Grouped metric details like &#x60;errors.mean&#x60;, &#x60;calls.sum&#x60;. It is usually a array of key-value pair. Format of key is &#x60;metric.aggregation.granularity&#x60;, for example: &#x60;latency.p75.360&#x60;. Format of value is &#x60;[earliest timestamp, value of key]&#x60;, for example: &#x60;[1725602720000, 0.013141001434936938]&#x60;.  | 
**name** | **str** | Name of the group. | 
**timestamp** | **int** | Earliest timestamp of the call from the group | [optional] 

## Example

```python
from instana_client.models.call_groups_item import CallGroupsItem

# TODO update the JSON string below
json = "{}"
# create an instance of CallGroupsItem from a JSON string
call_groups_item_instance = CallGroupsItem.from_json(json)
# print the JSON string representation of the object
print(CallGroupsItem.to_json())

# convert the object into a dict
call_groups_item_dict = call_groups_item_instance.to_dict()
# create an instance of CallGroupsItem from a dict
call_groups_item_from_dict = CallGroupsItem.from_dict(call_groups_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


