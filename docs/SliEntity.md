# SliEntity

Entity Type of the SLI Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sli_type** | **str** |  | 

## Example

```python
from instana_client.models.sli_entity import SliEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SliEntity from a JSON string
sli_entity_instance = SliEntity.from_json(json)
# print the JSON string representation of the object
print(SliEntity.to_json())

# convert the object into a dict
sli_entity_dict = sli_entity_instance.to_dict()
# create an instance of SliEntity from a dict
sli_entity_from_dict = SliEntity.from_dict(sli_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


