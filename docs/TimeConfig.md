# TimeConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_refresh** | **bool** |  | [optional] 
**focused_moment** | **int** |  | [optional] 
**to** | **int** |  | [optional] 
**window_size** | **int** |  | [optional] 

## Example

```python
from instana_client.models.time_config import TimeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TimeConfig from a JSON string
time_config_instance = TimeConfig.from_json(json)
# print the JSON string representation of the object
print(TimeConfig.to_json())

# convert the object into a dict
time_config_dict = time_config_instance.to_dict()
# create an instance of TimeConfig from a dict
time_config_from_dict = TimeConfig.from_dict(time_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


