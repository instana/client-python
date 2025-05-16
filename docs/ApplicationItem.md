# ApplicationItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**Application**](Application.md) |  | 
**metrics** | **Dict[str, List[List[float]]]** |  | 

## Example

```python
from instana_client.models.application_item import ApplicationItem

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationItem from a JSON string
application_item_instance = ApplicationItem.from_json(json)
# print the JSON string representation of the object
print(ApplicationItem.to_json())

# convert the object into a dict
application_item_dict = application_item_instance.to_dict()
# create an instance of ApplicationItem from a dict
application_item_from_dict = ApplicationItem.from_dict(application_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


