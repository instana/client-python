# NewManualServiceConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the manual service configuration. | [optional] 
**enabled** | **bool** | Enable or disable the manual service configuration. By default it is enabled. | [optional] 
**existing_service_id** | **str** | The service ID of the existing monitored service to which the calls should be linked. | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**unmonitored_service_name** | **str** | A service name if you want to map calls to an unmonitored service. | [optional] 

## Example

```python
from instana_client.models.new_manual_service_config import NewManualServiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NewManualServiceConfig from a JSON string
new_manual_service_config_instance = NewManualServiceConfig.from_json(json)
# print the JSON string representation of the object
print(NewManualServiceConfig.to_json())

# convert the object into a dict
new_manual_service_config_dict = new_manual_service_config_instance.to_dict()
# create an instance of NewManualServiceConfig from a dict
new_manual_service_config_from_dict = NewManualServiceConfig.from_dict(new_manual_service_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


