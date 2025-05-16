# SessionSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idle_time_in_millis** | **int** |  | [optional] 
**token_life_time_in_millis** | **int** |  | [optional] 

## Example

```python
from instana_client.models.session_settings import SessionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SessionSettings from a JSON string
session_settings_instance = SessionSettings.from_json(json)
# print the JSON string representation of the object
print(SessionSettings.to_json())

# convert the object into a dict
session_settings_dict = session_settings_instance.to_dict()
# create an instance of SessionSettings from a dict
session_settings_from_dict = SessionSettings.from_dict(session_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


