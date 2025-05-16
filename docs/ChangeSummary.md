# ChangeSummary

Brief summary of changes made in this config version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**Author**](Author.md) |  | 
**change_type** | **str** |  | 

## Example

```python
from instana_client.models.change_summary import ChangeSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeSummary from a JSON string
change_summary_instance = ChangeSummary.from_json(json)
# print the JSON string representation of the object
print(ChangeSummary.to_json())

# convert the object into a dict
change_summary_dict = change_summary_instance.to_dict()
# create an instance of ChangeSummary from a dict
change_summary_from_dict = ChangeSummary.from_dict(change_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


