# FilterInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rbac_restrictions** | [**RbacRestrictions**](RbacRestrictions.md) |  | [optional] 
**time_config** | [**TimeConfig**](TimeConfig.md) |  | [optional] 

## Example

```python
from instana_client.models.filter_interface import FilterInterface

# TODO update the JSON string below
json = "{}"
# create an instance of FilterInterface from a JSON string
filter_interface_instance = FilterInterface.from_json(json)
# print the JSON string representation of the object
print(FilterInterface.to_json())

# convert the object into a dict
filter_interface_dict = filter_interface_instance.to_dict()
# create an instance of FilterInterface from a dict
filter_interface_from_dict = FilterInterface.from_dict(filter_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


