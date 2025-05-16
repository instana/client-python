# MetaData

Action metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai** | **List[Dict[str, object]]** | List of metadata for AI originated actions. | [optional] 
**ai_originated** | **bool** | AI originated action flag. Value is &#x60;true&#x60; if action is AI generated &#x60;false&#x60; otherwise. | [optional] 
**built_in** | **bool** | Built-in out of the box action flag. Value is &#x60;true&#x60; if built-in action &#x60;false&#x60; otherwise. | [optional] 
**read_only** | **bool** | Read only action flag. Value is &#x60;true&#x60; if read only &#x60;false&#x60; otherwise. | [optional] 
**sensor_imported** | **bool** | Sensor imported action flag. Value is &#x60;true&#x60; if action is imported from sensor &#x60;false&#x60; otherwise. | [optional] 

## Example

```python
from instana_client.models.meta_data import MetaData

# TODO update the JSON string below
json = "{}"
# create an instance of MetaData from a JSON string
meta_data_instance = MetaData.from_json(json)
# print the JSON string representation of the object
print(MetaData.to_json())

# convert the object into a dict
meta_data_dict = meta_data_instance.to_dict()
# create an instance of MetaData from a dict
meta_data_from_dict = MetaData.from_dict(meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


