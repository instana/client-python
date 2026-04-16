# ApdexConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apdex_entity** | [**ApdexEntity**](ApdexEntity.md) |  | 
**apdex_name** | **str** |  | 
**created_at** | **int** | Created date of Apdex Configuration (Unix timestamp in milliseconds) | [optional] 
**id** | **str** | Apdex Configuration ID | 
**last_updated** | **int** | Last updated date of Apdex Configuration (Unix timestamp in milliseconds) | [optional] 
**tags** | **List[str]** | List of tags associated with Apdex Configuration | [optional] 

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


