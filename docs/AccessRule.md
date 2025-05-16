# AccessRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | Specifies the type of access permitted.   &#x60;READ&#x60;: Only viewing Application Perspective is allowed.   &#x60;READ_WRITE&#x60;: Both viewing and modifying Application Perspective are permitted.    | 
**related_id** | **str** | An identifier that connects the access rule to a specific entity. For example, if the &#x60;relationType&#x60; is &#x60;USER&#x60;, the corresponding &#x60;relatedId&#x60; would be a user id.   **Note**: when &#x60;relationType&#x60; is &#x60;GLOBAL&#x60;, &#x60;relatedId&#x60; is &#x60;null&#x60;.  | [optional] 
**relation_type** | **str** | Defines the type of relationship or subject to which the access rule applies.   &#x60;USER&#x60;: Access is granted to an individual user.   &#x60;API_TOKEN&#x60;: Access is granted to a specific API token.   &#x60;ROLE&#x60;: Access is granted based on a user role, applying to any user with that role.   &#x60;TEAM&#x60;: Access is granted to a team, likely applying to all team members.   &#x60;GLOBAL&#x60;: Access is granted to every user or service.  | 

## Example

```python
from instana_client.models.access_rule import AccessRule

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRule from a JSON string
access_rule_instance = AccessRule.from_json(json)
# print the JSON string representation of the object
print(AccessRule.to_json())

# convert the object into a dict
access_rule_dict = access_rule_instance.to_dict()
# create an instance of AccessRule from a dict
access_rule_from_dict = AccessRule.from_dict(access_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


