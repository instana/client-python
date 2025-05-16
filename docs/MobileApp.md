# MobileApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from instana_client.models.mobile_app import MobileApp

# TODO update the JSON string below
json = "{}"
# create an instance of MobileApp from a JSON string
mobile_app_instance = MobileApp.from_json(json)
# print the JSON string representation of the object
print(MobileApp.to_json())

# convert the object into a dict
mobile_app_dict = mobile_app_instance.to_dict()
# create an instance of MobileApp from a dict
mobile_app_from_dict = MobileApp.from_dict(mobile_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


