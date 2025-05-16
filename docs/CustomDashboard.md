# CustomDashboard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_rules** | [**List[AccessRule]**](AccessRule.md) |  | 
**id** | **str** |  | 
**title** | **str** |  | 
**widgets** | [**List[Widget]**](Widget.md) |  | 

## Example

```python
from instana_client.models.custom_dashboard import CustomDashboard

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDashboard from a JSON string
custom_dashboard_instance = CustomDashboard.from_json(json)
# print the JSON string representation of the object
print(CustomDashboard.to_json())

# convert the object into a dict
custom_dashboard_dict = custom_dashboard_instance.to_dict()
# create an instance of CustomDashboard from a dict
custom_dashboard_from_dict = CustomDashboard.from_dict(custom_dashboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


