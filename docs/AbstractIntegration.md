# AbstractIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the returned Alert Channel | 
**kind** | **str** | The type of the Alerting Channel. | 
**name** | **str** | The name of the Alerting Channel. | 

## Example

```python
from instana_client.models.abstract_integration import AbstractIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractIntegration from a JSON string
abstract_integration_instance = AbstractIntegration.from_json(json)
# print the JSON string representation of the object
print(AbstractIntegration.to_json())

# convert the object into a dict
abstract_integration_dict = abstract_integration_instance.to_dict()
# create an instance of AbstractIntegration from a dict
abstract_integration_from_dict = AbstractIntegration.from_dict(abstract_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


