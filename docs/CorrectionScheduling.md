# CorrectionScheduling

Time scheduling of the SLO Correction Window configurations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | Duration of the correction window, defined by the count of time units. | 
**duration_unit** | **str** | Unit for duration. Supported values: &#x60;MINUTE&#x60;, &#x60;HOUR&#x60;, &#x60;DAY&#x60;. | 
**recurrent** | **bool** |  | [optional] 
**recurrent_rule** | **str** | Recurrence Rule defines how the event recurs, using iCalendar RRULE format (e.g., &#x60;FREQ&#x3D;DAILY;INTERVAL&#x3D;1&#x60;).It supports fields like FREQ, INTERVAL, BYDAY, etc. Refer to RFC 5545: https://datatracker.ietf.org/doc/html/rfc5545#section-3.3.10 | [optional] 
**start_time** | **datetime** | Start time of the correction window in milliseconds since epoch (UTC) (e.g., &#x60;1706713140000&#x60;). | 

## Example

```python
from instana_client.models.correction_scheduling import CorrectionScheduling

# TODO update the JSON string below
json = "{}"
# create an instance of CorrectionScheduling from a JSON string
correction_scheduling_instance = CorrectionScheduling.from_json(json)
# print the JSON string representation of the object
print(CorrectionScheduling.to_json())

# convert the object into a dict
correction_scheduling_dict = correction_scheduling_instance.to_dict()
# create an instance of CorrectionScheduling from a dict
correction_scheduling_from_dict = CorrectionScheduling.from_dict(correction_scheduling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


