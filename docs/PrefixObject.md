# PrefixObject

Shortcode prefix configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | The prefix to use for event short codes (e.g., &#39;INSTANA-&#39;, &#39;PROD-&#39;) | [optional] 

## Example

```python
from instana_client.models.prefix_object import PrefixObject

# TODO update the JSON string below
json = "{}"
# create an instance of PrefixObject from a JSON string
prefix_object_instance = PrefixObject.from_json(json)
# print the JSON string representation of the object
print(PrefixObject.to_json())

# convert the object into a dict
prefix_object_dict = prefix_object_instance.to_dict()
# create an instance of PrefixObject from a dict
prefix_object_from_dict = PrefixObject.from_dict(prefix_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


