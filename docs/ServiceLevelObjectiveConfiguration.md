# ServiceLevelObjectiveConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** | Created date of Service Levels Objective Configuration | [optional] 
**entity** | [**SloEntity**](SloEntity.md) |  | 
**id** | **str** | Service Levels Objective Configuration ID | [optional] 
**indicator** | [**ServiceLevelIndicator**](ServiceLevelIndicator.md) |  | 
**last_updated** | **datetime** | Last updated date of Service Levels Objective Configuration | [optional] 
**name** | **str** | Name of the Service Levels Objective Configuration | 
**tags** | **List[str]** | List of tags associated with Service Levels Objective Configuration | 
**target** | **float** | Service Levels Objective Configuration Target | 
**time_window** | [**TimeWindow**](TimeWindow.md) |  | 

## Example

```python
from instana_client.models.service_level_objective_configuration import ServiceLevelObjectiveConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLevelObjectiveConfiguration from a JSON string
service_level_objective_configuration_instance = ServiceLevelObjectiveConfiguration.from_json(json)
# print the JSON string representation of the object
print(ServiceLevelObjectiveConfiguration.to_json())

# convert the object into a dict
service_level_objective_configuration_dict = service_level_objective_configuration_instance.to_dict()
# create an instance of ServiceLevelObjectiveConfiguration from a dict
service_level_objective_configuration_from_dict = ServiceLevelObjectiveConfiguration.from_dict(service_level_objective_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


