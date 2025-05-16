# SoftwareVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discovery_type** | **str** |  | 
**metadata** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | 
**plugin** | **str** |  | 
**software_type** | **str** |  | 
**used_by** | [**List[SoftwareUser]**](SoftwareUser.md) |  | 
**vendor** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from instana_client.models.software_version import SoftwareVersion

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareVersion from a JSON string
software_version_instance = SoftwareVersion.from_json(json)
# print the JSON string representation of the object
print(SoftwareVersion.to_json())

# convert the object into a dict
software_version_dict = software_version_instance.to_dict()
# create an instance of SoftwareVersion from a dict
software_version_from_dict = SoftwareVersion.from_dict(software_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


