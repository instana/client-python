# ICMPValidation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**operator** | **str** |  | 
**value** | **int** |  | 

## Example

```python
from instana_client.models.icmp_validation import ICMPValidation

# TODO update the JSON string below
json = "{}"
# create an instance of ICMPValidation from a JSON string
icmp_validation_instance = ICMPValidation.from_json(json)
# print the JSON string representation of the object
print(ICMPValidation.to_json())

# convert the object into a dict
icmp_validation_dict = icmp_validation_instance.to_dict()
# create an instance of ICMPValidation from a dict
icmp_validation_from_dict = ICMPValidation.from_dict(icmp_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


