# HttpEndpointRule

Specify custom rule configuration apart from Instana predefined rules. This rule has the highest precedence. This is only available for HTTP endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Set this flag to &#x60;true&#x60; if custom rule configurations has to be considered. | [optional] 
**path_segments** | [**List[HttpPathSegmentMatchingRule]**](HttpPathSegmentMatchingRule.md) | A list of path segment matching rules, each defining how a segment of the HTTP path should be matched. Each object in this array represents a segment rule, allowing for fixed segments, dynamic parameters, wildcards, or unsupported segments.   **UNSUPPORTED**: A path segment that is not recognized by the system.   **FIXED**: This type represents a static, unchanging part of the URL path. For example, &#x60;/api/{version}/users&#x60;, &#x60;api&#x60; and &#x60;users&#x60; would be &#x60;FIXED&#x60; segment.   **PARAMETER**: This type represents a variable part of the URL path, often used to capture specific parameters or IDs that change with each request. For example, &#x60;/api/{version}/users&#x60;, &#x60;version&#x60; would be &#x60;PARAMETER&#x60; segment. &#x60;version&#x60; can be &#x60;v1&#x60;, &#x60;v2&#x60;, &#x60;v3&#x60; etc.   **MATCH_ALL**: This type represents a wildcard, capturing all remaining segments from this point onward in the URL path. For example, &#x60;/api/{version}/users/*&#x60; — Matches all paths like &#x60;/api/v1/users/123&#x60;. &#x60;/api/v3/users/456&#x60; etc.    | 
**test_cases** | **List[str]** | To validate whether the the defined custom endpoint rule configuration is working as expected. For example, given a query &#x60;/api/*/{version}&#x60;, the following test case &#x60;/api/anyName/123&#x60; will match, while &#x60;/otherApi/anyName/123&#x60; will not.  | [optional] 

## Example

```python
from instana_client.models.http_endpoint_rule import HttpEndpointRule

# TODO update the JSON string below
json = "{}"
# create an instance of HttpEndpointRule from a JSON string
http_endpoint_rule_instance = HttpEndpointRule.from_json(json)
# print the JSON string representation of the object
print(HttpEndpointRule.to_json())

# convert the object into a dict
http_endpoint_rule_dict = http_endpoint_rule_instance.to_dict()
# create an instance of HttpEndpointRule from a dict
http_endpoint_rule_from_dict = HttpEndpointRule.from_dict(http_endpoint_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


