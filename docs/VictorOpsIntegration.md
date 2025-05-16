# VictorOpsIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | 
**routing_key** | **str** |  | 

## Example

```python
from instana_client.models.victor_ops_integration import VictorOpsIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of VictorOpsIntegration from a JSON string
victor_ops_integration_instance = VictorOpsIntegration.from_json(json)
# print the JSON string representation of the object
print(VictorOpsIntegration.to_json())

# convert the object into a dict
victor_ops_integration_dict = victor_ops_integration_instance.to_dict()
# create an instance of VictorOpsIntegration from a dict
victor_ops_integration_from_dict = VictorOpsIntegration.from_dict(victor_ops_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


