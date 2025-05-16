# PathParameterHttpPathSegmentMatchingRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Given &#x60;/api/{version}/users&#x60; URI, &#x60;PARAMETER&#x60; name is &#x60;version&#x60;.  | 

## Example

```python
from instana_client.models.path_parameter_http_path_segment_matching_rule import PathParameterHttpPathSegmentMatchingRule

# TODO update the JSON string below
json = "{}"
# create an instance of PathParameterHttpPathSegmentMatchingRule from a JSON string
path_parameter_http_path_segment_matching_rule_instance = PathParameterHttpPathSegmentMatchingRule.from_json(json)
# print the JSON string representation of the object
print(PathParameterHttpPathSegmentMatchingRule.to_json())

# convert the object into a dict
path_parameter_http_path_segment_matching_rule_dict = path_parameter_http_path_segment_matching_rule_instance.to_dict()
# create an instance of PathParameterHttpPathSegmentMatchingRule from a dict
path_parameter_http_path_segment_matching_rule_from_dict = PathParameterHttpPathSegmentMatchingRule.from_dict(path_parameter_http_path_segment_matching_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


