# UsageResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UsageResultItems]**](UsageResultItems.md) |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from instana_client.models.usage_result import UsageResult

# TODO update the JSON string below
json = "{}"
# create an instance of UsageResult from a JSON string
usage_result_instance = UsageResult.from_json(json)
# print the JSON string representation of the object
print(UsageResult.to_json())

# convert the object into a dict
usage_result_dict = usage_result_instance.to_dict()
# create an instance of UsageResult from a dict
usage_result_from_dict = UsageResult.from_dict(usage_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


