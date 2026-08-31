# MobileSloEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mobile_ids** | **List[str]** | The ID(s) of the Mobile Apps | [optional] 

## Example

```python
from instana_client.models.mobile_slo_entity import MobileSloEntity

# TODO update the JSON string below
json = "{}"
# create an instance of MobileSloEntity from a JSON string
mobile_slo_entity_instance = MobileSloEntity.from_json(json)
# print the JSON string representation of the object
print(MobileSloEntity.to_json())

# convert the object into a dict
mobile_slo_entity_dict = mobile_slo_entity_instance.to_dict()
# create an instance of MobileSloEntity from a dict
mobile_slo_entity_from_dict = MobileSloEntity.from_dict(mobile_slo_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


