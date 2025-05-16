# PrometheusWebhookIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receiver** | **str** |  | [optional] 
**webhook_url** | **str** |  | 

## Example

```python
from instana_client.models.prometheus_webhook_integration import PrometheusWebhookIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusWebhookIntegration from a JSON string
prometheus_webhook_integration_instance = PrometheusWebhookIntegration.from_json(json)
# print the JSON string representation of the object
print(PrometheusWebhookIntegration.to_json())

# convert the object into a dict
prometheus_webhook_integration_dict = prometheus_webhook_integration_instance.to_dict()
# create an instance of PrometheusWebhookIntegration from a dict
prometheus_webhook_integration_from_dict = PrometheusWebhookIntegration.from_dict(prometheus_webhook_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


