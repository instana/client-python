# UsageResultItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**sims** | **int** |  | [optional] 

## Example

```python
from instana_client.models.usage_result_items import UsageResultItems

# TODO update the JSON string below
json = "{}"
# create an instance of UsageResultItems from a JSON string
usage_result_items_instance = UsageResultItems.from_json(json)
# print the JSON string representation of the object
print(UsageResultItems.to_json())

# convert the object into a dict
usage_result_items_dict = usage_result_items_instance.to_dict()
# create an instance of UsageResultItems from a dict
usage_result_items_from_dict = UsageResultItems.from_dict(usage_result_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


