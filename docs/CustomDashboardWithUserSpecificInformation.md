# CustomDashboardWithUserSpecificInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_rules** | [**List[AccessRule]**](AccessRule.md) |  | 
**id** | **str** |  | 
**owner_id** | **str** |  | 
**title** | **str** |  | 
**widgets** | [**List[Widget]**](Widget.md) |  | 
**writable** | **bool** |  | 

## Example

```python
from instana_client.models.custom_dashboard_with_user_specific_information import CustomDashboardWithUserSpecificInformation

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDashboardWithUserSpecificInformation from a JSON string
custom_dashboard_with_user_specific_information_instance = CustomDashboardWithUserSpecificInformation.from_json(json)
# print the JSON string representation of the object
print(CustomDashboardWithUserSpecificInformation.to_json())

# convert the object into a dict
custom_dashboard_with_user_specific_information_dict = custom_dashboard_with_user_specific_information_instance.to_dict()
# create an instance of CustomDashboardWithUserSpecificInformation from a dict
custom_dashboard_with_user_specific_information_from_dict = CustomDashboardWithUserSpecificInformation.from_dict(custom_dashboard_with_user_specific_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


