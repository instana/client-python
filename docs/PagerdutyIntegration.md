# PagerdutyIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_integration_key** | **str** |  | 

## Example

```python
from instana_client.models.pagerduty_integration import PagerdutyIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of PagerdutyIntegration from a JSON string
pagerduty_integration_instance = PagerdutyIntegration.from_json(json)
# print the JSON string representation of the object
print(PagerdutyIntegration.to_json())

# convert the object into a dict
pagerduty_integration_dict = pagerduty_integration_instance.to_dict()
# create an instance of PagerdutyIntegration from a dict
pagerduty_integration_from_dict = PagerdutyIntegration.from_dict(pagerduty_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


