# EntityHealthInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_severity** | **float** |  | [optional] 
**open_issues** | [**List[Event]**](Event.md) |  | 

## Example

```python
from instana_client.models.entity_health_info import EntityHealthInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EntityHealthInfo from a JSON string
entity_health_info_instance = EntityHealthInfo.from_json(json)
# print the JSON string representation of the object
print(EntityHealthInfo.to_json())

# convert the object into a dict
entity_health_info_dict = entity_health_info_instance.to_dict()
# create an instance of EntityHealthInfo from a dict
entity_health_info_from_dict = EntityHealthInfo.from_dict(entity_health_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


