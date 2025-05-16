# ApdexConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apdex_entity** | [**ApdexEntity**](ApdexEntity.md) |  | 
**apdex_name** | **str** | Name of the Apdex Configuration | 
**created_at** | **int** | Created Date of Apdex Configuration | [optional] 
**id** | **str** | Apdex Configuration ID | 

## Example

```python
from instana_client.models.apdex_configuration import ApdexConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ApdexConfiguration from a JSON string
apdex_configuration_instance = ApdexConfiguration.from_json(json)
# print the JSON string representation of the object
print(ApdexConfiguration.to_json())

# convert the object into a dict
apdex_configuration_dict = apdex_configuration_instance.to_dict()
# create an instance of ApdexConfiguration from a dict
apdex_configuration_from_dict = ApdexConfiguration.from_dict(apdex_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


