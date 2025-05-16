# DatabaseIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from instana_client.models.database_integration import DatabaseIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseIntegration from a JSON string
database_integration_instance = DatabaseIntegration.from_json(json)
# print the JSON string representation of the object
print(DatabaseIntegration.to_json())

# convert the object into a dict
database_integration_dict = database_integration_instance.to_dict()
# create an instance of DatabaseIntegration from a dict
database_integration_from_dict = DatabaseIntegration.from_dict(database_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


