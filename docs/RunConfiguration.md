# RunConfiguration

Action run configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[ActionConfiguration]**](ActionConfiguration.md) | List of action configurations. | 

## Example

```python
from instana_client.models.run_configuration import RunConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RunConfiguration from a JSON string
run_configuration_instance = RunConfiguration.from_json(json)
# print the JSON string representation of the object
print(RunConfiguration.to_json())

# convert the object into a dict
run_configuration_dict = run_configuration_instance.to_dict()
# create an instance of RunConfiguration from a dict
run_configuration_from_dict = RunConfiguration.from_dict(run_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


