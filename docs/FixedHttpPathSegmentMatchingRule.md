# FixedHttpPathSegmentMatchingRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Given &#x60;/api/{version}/users&#x60; URI, &#x60;FIXED&#x60; names are &#x60;api&#x60; and &#x60;users&#x60; in order.  | 

## Example

```python
from instana_client.models.fixed_http_path_segment_matching_rule import FixedHttpPathSegmentMatchingRule

# TODO update the JSON string below
json = "{}"
# create an instance of FixedHttpPathSegmentMatchingRule from a JSON string
fixed_http_path_segment_matching_rule_instance = FixedHttpPathSegmentMatchingRule.from_json(json)
# print the JSON string representation of the object
print(FixedHttpPathSegmentMatchingRule.to_json())

# convert the object into a dict
fixed_http_path_segment_matching_rule_dict = fixed_http_path_segment_matching_rule_instance.to_dict()
# create an instance of FixedHttpPathSegmentMatchingRule from a dict
fixed_http_path_segment_matching_rule_from_dict = FixedHttpPathSegmentMatchingRule.from_dict(fixed_http_path_segment_matching_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


