# DashboardApiToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from instana_client.models.dashboard_api_token import DashboardApiToken

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardApiToken from a JSON string
dashboard_api_token_instance = DashboardApiToken.from_json(json)
# print the JSON string representation of the object
print(DashboardApiToken.to_json())

# convert the object into a dict
dashboard_api_token_dict = dashboard_api_token_instance.to_dict()
# create an instance of DashboardApiToken from a dict
dashboard_api_token_from_dict = DashboardApiToken.from_dict(dashboard_api_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


