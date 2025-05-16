# SplunkIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from instana_client.models.splunk_integration import SplunkIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of SplunkIntegration from a JSON string
splunk_integration_instance = SplunkIntegration.from_json(json)
# print the JSON string representation of the object
print(SplunkIntegration.to_json())

# convert the object into a dict
splunk_integration_dict = splunk_integration_instance.to_dict()
# create an instance of SplunkIntegration from a dict
splunk_integration_from_dict = SplunkIntegration.from_dict(splunk_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


