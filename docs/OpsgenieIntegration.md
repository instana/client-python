# OpsgenieIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 
**api_key** | **str** |  | 
**region** | **str** |  | 
**tags** | **str** |  | [optional] 

## Example

```python
from instana_client.models.opsgenie_integration import OpsgenieIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of OpsgenieIntegration from a JSON string
opsgenie_integration_instance = OpsgenieIntegration.from_json(json)
# print the JSON string representation of the object
print(OpsgenieIntegration.to_json())

# convert the object into a dict
opsgenie_integration_dict = opsgenie_integration_instance.to_dict()
# create an instance of OpsgenieIntegration from a dict
opsgenie_integration_from_dict = OpsgenieIntegration.from_dict(opsgenie_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


