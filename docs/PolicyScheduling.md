# PolicyScheduling

Scheduling information for a scheduled policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recurrent_rule** | **str** | Recurrent Rule defines how the policy recurs, using iCalendar RRULE format (e.g., &#x60;FREQ&#x3D;DAILY;INTERVAL&#x3D;1&#x60;).It supports fields like FREQ, INTERVAL, BYDAY. Refer to RFC 5545: https://datatracker.ietf.org/doc/html/rfc5545#section-3.3.10 | [optional] 
**start_time** | **datetime** | The time to run the policy action in milliseconds since epoch (UTC) (e.g., &#x60;1706713140000&#x60;). | 

## Example

```python
from instana_client.models.policy_scheduling import PolicyScheduling

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyScheduling from a JSON string
policy_scheduling_instance = PolicyScheduling.from_json(json)
# print the JSON string representation of the object
print(PolicyScheduling.to_json())

# convert the object into a dict
policy_scheduling_dict = policy_scheduling_instance.to_dict()
# create an instance of PolicyScheduling from a dict
policy_scheduling_from_dict = PolicyScheduling.from_dict(policy_scheduling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


