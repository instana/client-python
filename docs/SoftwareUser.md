# SoftwareUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**process** | **str** |  | [optional] 
**snapshot_id** | **str** |  | [optional] 

## Example

```python
from instana_client.models.software_user import SoftwareUser

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareUser from a JSON string
software_user_instance = SoftwareUser.from_json(json)
# print the JSON string representation of the object
print(SoftwareUser.to_json())

# convert the object into a dict
software_user_dict = software_user_instance.to_dict()
# create an instance of SoftwareUser from a dict
software_user_from_dict = SoftwareUser.from_dict(software_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


