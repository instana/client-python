# SliConfigurationWithLastUpdated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID for each SLI | 
**initial_evaluation_timestamp** | **int** | Initial evaluation timestamp in milliseconds (13-digit) | [optional] 
**last_updated** | **int** | Last Updated timestamp in milliseconds (13-digit) | [optional] 
**metric_configuration** | [**MetricConfiguration**](MetricConfiguration.md) |  | [optional] 
**sli_entity** | [**SliEntity**](SliEntity.md) |  | 
**sli_name** | **str** | The name of the Service Level Indicator (SLI) specified during its creation | 

## Example

```python
from instana_client.models.sli_configuration_with_last_updated import SliConfigurationWithLastUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of SliConfigurationWithLastUpdated from a JSON string
sli_configuration_with_last_updated_instance = SliConfigurationWithLastUpdated.from_json(json)
# print the JSON string representation of the object
print(SliConfigurationWithLastUpdated.to_json())

# convert the object into a dict
sli_configuration_with_last_updated_dict = sli_configuration_with_last_updated_instance.to_dict()
# create an instance of SliConfigurationWithLastUpdated from a dict
sli_configuration_with_last_updated_from_dict = SliConfigurationWithLastUpdated.from_dict(sli_configuration_with_last_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


