# ServiceLevelsBurnRateTimeWindows

This is the short and long time window setting for the burn rate alerts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**long_time_window** | [**AlertingTimeWindow**](AlertingTimeWindow.md) |  | [optional] 
**short_time_window** | [**AlertingTimeWindow**](AlertingTimeWindow.md) |  | [optional] 

## Example

```python
from instana_client.models.service_levels_burn_rate_time_windows import ServiceLevelsBurnRateTimeWindows

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLevelsBurnRateTimeWindows from a JSON string
service_levels_burn_rate_time_windows_instance = ServiceLevelsBurnRateTimeWindows.from_json(json)
# print the JSON string representation of the object
print(ServiceLevelsBurnRateTimeWindows.to_json())

# convert the object into a dict
service_levels_burn_rate_time_windows_dict = service_levels_burn_rate_time_windows_instance.to_dict()
# create an instance of ServiceLevelsBurnRateTimeWindows from a dict
service_levels_burn_rate_time_windows_from_dict = ServiceLevelsBurnRateTimeWindows.from_dict(service_levels_burn_rate_time_windows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


