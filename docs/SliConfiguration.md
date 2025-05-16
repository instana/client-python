# SliConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID for each SLI | 
**initial_evaluation_timestamp** | **int** | Initial evaluation timestamp in milliseconds (13-digit) | [optional] 
**metric_configuration** | [**MetricConfiguration**](MetricConfiguration.md) |  | [optional] 
**sli_entity** | [**SliEntity**](SliEntity.md) |  | 
**sli_name** | **str** | The name of the Service Level Indicator (SLI) specified during its creation | 

## Example

```python
from instana_client.models.sli_configuration import SliConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SliConfiguration from a JSON string
sli_configuration_instance = SliConfiguration.from_json(json)
# print the JSON string representation of the object
print(SliConfiguration.to_json())

# convert the object into a dict
sli_configuration_dict = sli_configuration_instance.to_dict()
# create an instance of SliConfiguration from a dict
sli_configuration_from_dict = SliConfiguration.from_dict(sli_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


