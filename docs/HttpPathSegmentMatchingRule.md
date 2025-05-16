# HttpPathSegmentMatchingRule

A list of path segment matching rules, each defining how a segment of the HTTP path should be matched. Each object in this array represents a segment rule, allowing for fixed segments, dynamic parameters, wildcards, or unsupported segments.   **UNSUPPORTED**: A path segment that is not recognized by the system.   **FIXED**: This type represents a static, unchanging part of the URL path. For example, `/api/{version}/users`, `api` and `users` would be `FIXED` segment.   **PARAMETER**: This type represents a variable part of the URL path, often used to capture specific parameters or IDs that change with each request. For example, `/api/{version}/users`, `version` would be `PARAMETER` segment. `version` can be `v1`, `v2`, `v3` etc.   **MATCH_ALL**: This type represents a wildcard, capturing all remaining segments from this point onward in the URL path. For example, `/api/{version}/users/*` — Matches all paths like `/api/v1/users/123`. `/api/v3/users/456` etc.   

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from instana_client.models.http_path_segment_matching_rule import HttpPathSegmentMatchingRule

# TODO update the JSON string below
json = "{}"
# create an instance of HttpPathSegmentMatchingRule from a JSON string
http_path_segment_matching_rule_instance = HttpPathSegmentMatchingRule.from_json(json)
# print the JSON string representation of the object
print(HttpPathSegmentMatchingRule.to_json())

# convert the object into a dict
http_path_segment_matching_rule_dict = http_path_segment_matching_rule_instance.to_dict()
# create an instance of HttpPathSegmentMatchingRule from a dict
http_path_segment_matching_rule_from_dict = HttpPathSegmentMatchingRule.from_dict(http_path_segment_matching_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


