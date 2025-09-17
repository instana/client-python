# CustomEntityWithMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** |  | [optional] 
**data** | [**CustomEntityModel**](CustomEntityModel.md) |  | 
**id** | **str** |  | 
**version** | **str** |  | [optional] 

## Example

```python
from instana_client.models.custom_entity_with_metadata import CustomEntityWithMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEntityWithMetadata from a JSON string
custom_entity_with_metadata_instance = CustomEntityWithMetadata.from_json(json)
# print the JSON string representation of the object
print(CustomEntityWithMetadata.to_json())

# convert the object into a dict
custom_entity_with_metadata_dict = custom_entity_with_metadata_instance.to_dict()
# create an instance of CustomEntityWithMetadata from a dict
custom_entity_with_metadata_from_dict = CustomEntityWithMetadata.from_dict(custom_entity_with_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


