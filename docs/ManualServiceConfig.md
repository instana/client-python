# ManualServiceConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the manual service configuration. | [optional] 
**enabled** | **bool** | Enable or disable the manual service configuration. By default it is enabled. | [optional] 
**existing_service_id** | **str** | The service ID of the existing monitored service to which the calls should be linked. | [optional] 
**id** | **str** | A unique id of the manual service configuration. | 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**unmonitored_service_name** | **str** | A service name if you want to map calls to an unmonitored service. | [optional] 

## Example

```python
from instana_client.models.manual_service_config import ManualServiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ManualServiceConfig from a JSON string
manual_service_config_instance = ManualServiceConfig.from_json(json)
# print the JSON string representation of the object
print(ManualServiceConfig.to_json())

# convert the object into a dict
manual_service_config_dict = manual_service_config_instance.to_dict()
# create an instance of ManualServiceConfig from a dict
manual_service_config_from_dict = ManualServiceConfig.from_dict(manual_service_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


